from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import LostItemForm, FoundItemForm
from .models import LostItem, FoundItem
from django.db.models import Q

@login_required
def found_item_upload(request):
    if request.method == "POST":
        form = FoundItemForm(request.POST, request.FILES)
        if form.is_valid():
            found_item = form.save(commit=False)
            found_item.user = request.user
            found_item.save()
            return redirect("accounts:home")  
    else:
        form = FoundItemForm()

    return render(request, "found.html", {"form": form})

@login_required
def lost_item_upload(request):
    if request.method == "POST":
        form = LostItemForm(request.POST, request.FILES)
        if form.is_valid():
            lost_item = form.save(commit=False)
            lost_item.user = request.user
            lost_item.save()
            return redirect("items:lost_and_found_list")
        else:
            print(form.errors)
    else:
        form = LostItemForm()

    return render(request, "lost.html", {"form": form})

@login_required
def lost_and_found_list(request):
    query = request.GET.get('q', '')

    lost_items = LostItem.objects.all()
    found_items = FoundItem.objects.all()

    if query:
        lost_items = lost_items.filter(
            Q(name__icontains=query) |
            Q(category__name__icontains=query) |
            Q(last_location__icontains=query)
        )
        found_items = found_items.filter(
            Q(name__icontains=query) |
            Q(category__name__icontains=query) |
            Q(found_location__icontains=query)
        )

    items = []

    for item in lost_items:
        items.append({
            "id": item.id,
            "name": item.name,
            "category": item.category.name if item.category else "",
            "description": item.description,
            "location": item.last_location,
            "date": item.lost_date,
            "image": item.image.url,
            "status": "lost",
        })

    for item in found_items:
        items.append({
            "id": item.id,
            "name": item.name,
            "category": item.category.name if item.category else "",
            "description": item.description,
            "location": item.found_location,
            "date": item.date_found,
            "image": item.image.url,
            "status": "found",
        })

    items.sort(key=lambda x: x["date"], reverse=True)

    return render(request, "search.html", {"items": items, "query": query})

@login_required
def item_detail(request, item_type, item_id):
    if item_type == "lost":
        item = get_object_or_404(LostItem, id=item_id)
        status = "LOST"
        location = item.last_location
        date = item.lost_date
        item_status = "lost"  # <-- add this
    elif item_type == "found":
        item = get_object_or_404(FoundItem, id=item_id)
        status = "FOUND"
        location = item.found_location
        date = item.date_found
        item_status = "found"  # <-- add this
    else:
        return render(request, "404.html")  # invalid type

    context = {
        "item": item,
        "status": status,
        "location": location,
        "date": date,
        "item_status": item_status,  # <-- pass to template
    }

    return render(request, "detail-card.html", context)
