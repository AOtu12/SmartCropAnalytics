from django.shortcuts import render
from django.db.models import Q, Sum, Avg
from .models import CropData
import json


# This function handles the main data table page
# It displays crop records and allows filtering + sorting

def data_page(request):
    # Get all crop records from the database
    crops = CropData.objects.all()

    # Get filter values from the URL (GET request)
    year = request.GET.get('year')
    region = request.GET.get('region')
    search = request.GET.get('search')
    sort = request.GET.get('sort')

    # Apply year filter if selected
    if year:
        crops = crops.filter(year=year)

    # Apply region filter if selected
    if region:
        crops = crops.filter(region=region)

    # Search by crop name or region name
    if search:
        crops = crops.filter(
            Q(crop__icontains=search) |
            Q(region__icontains=search)
        )

    # Sort results based on user selection
    if sort == 'production':
        # Highest production first
        crops = crops.order_by('-production')
    elif sort == 'yield':
        # Highest yield first
        crops = crops.order_by('-yield_amount')

    # Get unique years and regions for dropdown filters
    years = CropData.objects.values_list('year', flat=True).distinct()
    regions = CropData.objects.values_list('region', flat=True).distinct()

    # Send data to the HTML template
    return render(request, 'crops/data.html', {
        'crops': crops,
        'years': years,
        'regions': regions,
    })


# This function handles the charts dashboard page
# It creates chart data based on filters selected by the user

def chart_page(request):
    # Start with all crop records
    crops = CropData.objects.all()

    # Get selected filter values from the charts page
    year = request.GET.get('year')
    region = request.GET.get('region')
    crop_name = request.GET.get('crop')

    # Apply year filter if selected
    if year:
        crops = crops.filter(year=year)

    # Apply region filter if selected
    if region:
        crops = crops.filter(region=region)

    # Apply crop filter if selected
    if crop_name:
        crops = crops.filter(crop=crop_name)

    # Get dropdown values for filter options
    years = CropData.objects.values_list('year', flat=True).distinct()
    regions = CropData.objects.values_list('region', flat=True).distinct()
    crop_names = CropData.objects.values_list('crop', flat=True).distinct()

    # CHART 1: Total production grouped by crop
    production_data = (
        crops.values('crop')
        .annotate(total_production=Sum('production'))
        .filter(total_production__isnull=False)
        .order_by('-total_production')[:10]  # Top 10 crops only
    )

    # Extract labels and values for Chart.js
    production_labels = [item['crop'] for item in production_data]
    production_values = [item['total_production'] or 0 for item in production_data]

    # CHART 2: Average yield grouped by year
    yield_data = (
        crops.values('year')
        .annotate(avg_yield=Avg('yield_amount'))
        .filter(avg_yield__isnull=False)
        .order_by('year')
    )

    # Extract labels and values for yield chart
    yield_labels = [item['year'] for item in yield_data]
    yield_values = [float(item['avg_yield'] or 0) for item in yield_data]

    # CHART 3: Total production grouped by region
    region_data = (
        crops.values('region')
        .annotate(total_production=Sum('production'))
        .filter(total_production__isnull=False, total_production__gt=0)
        .order_by('-total_production')
    )

    # Extract labels and values for region chart
    region_labels = [item['region'] for item in region_data]
    region_values = [item['total_production'] or 0 for item in region_data]

    # Convert Python lists into JSON so JavaScript can use them in Chart.js
    return render(request, 'crops/charts.html', {
        'years': years,
        'regions': regions,
        'crop_names': crop_names,

        'production_labels': json.dumps(production_labels),
        'production_values': json.dumps(production_values),

        'yield_labels': json.dumps(yield_labels),
        'yield_values': json.dumps(yield_values),

        'region_labels': json.dumps(region_labels),
        'region_values': json.dumps(region_values),
    })