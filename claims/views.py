from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Claim
from items.models import LostItem, FoundItem

@login_required
def claim_item(request, item_type, item_id):
    """
    Handles both lost and found item claims.
    item_type: 'lost' or 'found'
    """
    if item_type == 'lost':
        item = get_object_or_404(LostItem, id=item_id)
        existing_claim = Claim.objects.filter(user=request.user, lost_item=item).first()
    elif item_type == 'found':
        item = get_object_or_404(FoundItem, id=item_id)
        existing_claim = Claim.objects.filter(user=request.user, found_item=item).first()
    else:
        return redirect('items:lost_and_found_list')  # fallback

    if existing_claim:
        # Already claimed → go to my_claims
        return redirect(f'/claims/my_claims/?claimed_id={existing_claim.id}')

    if request.method == "POST":
        if item_type == 'lost':
            claim = Claim.objects.create(user=request.user, lost_item=item)
        else:
            claim = Claim.objects.create(user=request.user, found_item=item)

        return redirect(f'/claims/my_claims/?claimed_id={claim.id}')

    return render(request, "claim-item.html", {"item": item, "type": item_type})

@login_required
def my_claims(request):
    claims = Claim.objects.filter(user=request.user).order_by('-created_at')
    claimed_id = request.GET.get('claimed_id')  # highlight a specific claim
    return render(request, "my_claims.html", {"claims": claims, "claimed_id": claimed_id})
