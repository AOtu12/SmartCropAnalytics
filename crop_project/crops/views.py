from django.shortcuts import render
from django.db.models import Q, Sum, Avg
from .models import CropData
import json


# =========================
# DATA PAGE (TABLE)
# =========================
def data_page(request):
    # Get all data
    crops = CropData.objects.all()

    # Get filters from URL
    year = request.GET.get('year')
    region = request.GET.get('region')
    search = request.GET.get('search')
    sort = request.GET.get('sort')

    # Apply filters
    if year:
        crops = crops.filter(year=year)

    if region:
        crops = crops.filter(region=region)

    # Search functionality
    if search:
        crops = crops.filter(
            Q(crop__icontains=search) |
            Q(region__icontains=search)
        )

    # Sorting
    if sort == 'production':
        crops = crops.order_by('-production')
    elif sort == 'yield':
        crops = crops.order_by('-yield_amount')

    # Dropdown values
    years = CropData.objects.values_list('year', flat=True).distinct()
    regions = CropData.objects.values_list('region', flat=True).distinct()

    return render(request, 'crops/data.html', {
        'crops': crops,
        'years': years,
        'regions': regions,
    })


# =========================
# CHART PAGE (DASHBOARD)
# =========================
def chart_page(request):
    # Start with all data
    crops = CropData.objects.all()

    # Get filter values
    year = request.GET.get('year')
    region = request.GET.get('region')
    crop_name = request.GET.get('crop')

    # Apply filters
    if year:
        crops = crops.filter(year=year)

    if region:
        crops = crops.filter(region=region)

    if crop_name:
        crops = crops.filter(crop=crop_name)

    # Dropdown data
    years = CropData.objects.values_list('year', flat=True).distinct()
    regions = CropData.objects.values_list('region', flat=True).distinct()
    crop_names = CropData.objects.values_list('crop', flat=True).distinct()

    # =========================
    # CHART 1: PRODUCTION BY CROP
    # =========================
    production_data = (
        crops.values('crop')
        .annotate(total_production=Sum('production'))
        .filter(total_production__isnull=False)
        .order_by('-total_production')[:10]
    )

    # Handle empty results (VERY IMPORTANT)
    if not production_data:
        production_labels = ["No Data"]
        production_values = [0]
    else:
        production_labels = [item['crop'] for item in production_data]
        production_values = [item['total_production'] or 0 for item in production_data]

    # =========================
    # CHART 2: YIELD OVER TIME
    # =========================
    yield_data = (
        crops.values('year')
        .annotate(avg_yield=Avg('yield_amount'))
        .filter(avg_yield__isnull=False)
        .order_by('year')
    )

    if not yield_data:
        yield_labels = ["No Data"]
        yield_values = [0]
    else:
        yield_labels = [item['year'] for item in yield_data]
        yield_values = [float(item['avg_yield'] or 0) for item in yield_data]

    # =========================
    # CHART 3: PRODUCTION BY REGION
    # =========================
    region_data = (
        crops.values('region')
        .annotate(total_production=Sum('production'))
        .filter(total_production__isnull=False)
        .order_by('-total_production')
    )

    if not region_data:
        region_labels = ["No Data"]
        region_values = [0]
    else:
        region_labels = [item['region'] for item in region_data]
        region_values = [item['total_production'] or 0 for item in region_data]

    # Send everything to frontend
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