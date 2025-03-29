from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Reservation, Table, Customer, Menu
from .forms import ReservationForm, UserRegisterForm
from datetime import datetime, date, time


# Create your views here.
def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            Customer.objects.create(
                user=user,
                phone_number=form.cleaned_data['phone_number']
            )
            messages.success(request, 'Account created successfully! You can now log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

@login_required
def reservation_list(request):
    customer = Customer.objects.get(user=request.user)
    reservations = Reservation.objects.filter(customer=customer, is_cancelled=False)
    return render(request, 'reservations/list.html', {'reservations': reservations})

@login_required
def create_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            customer = Customer.objects.get(user=request.user)
            reservation.customer = customer
            
            # Check for overlapping reservations
            overlapping = Reservation.objects.filter(
                table=reservation.table,
                date=reservation.date,
                is_cancelled=False,
                start_time__lt=reservation.end_time,
                end_time__gt=reservation.start_time
            ).exists()
            
            if not overlapping:
                reservation.save()
                messages.success(request, 'Reservation created successfully!')
                return redirect('reservation_list')
            else:
                messages.error(request, 'This table is already booked for the selected time.')
    else:
        form = ReservationForm()
    
    return render(request, 'reservations/create.html', {'form': form})

@login_required
def edit_reservation(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk, customer__user=request.user)
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            updated_reservation = form.save(commit=False)
            
            # Check for overlapping reservations excluding current one
            overlapping = Reservation.objects.filter(
                table=updated_reservation.table,
                date=updated_reservation.date,
                is_cancelled=False,
                start_time__lt=updated_reservation.end_time,
                end_time__gt=updated_reservation.start_time
            ).exclude(pk=reservation.pk).exists()
            
            if not overlapping:
                updated_reservation.save()
                messages.success(request, 'Reservation updated successfully!')
                return redirect('reservation_list')
            else:
                messages.error(request, 'This table is already booked for the selected time.')
    else:
        form = ReservationForm(instance=reservation)
    
    return render(request, 'reservations/edit.html', {'form': form, 'reservation': reservation})

@login_required
def cancel_reservation(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk, customer__user=request.user)
    if request.method == 'POST':
        reservation.is_cancelled = True
        reservation.save()
        messages.success(request, 'Reservation cancelled successfully!')
        return redirect('reservation_list')
    return render(request, 'reservations/cancel.html', {'reservation': reservation})

def menu(request):
    menu_items = Menu.objects.filter(is_available=True)
    return render(request, 'menu.html', {'menu_items': menu_items})