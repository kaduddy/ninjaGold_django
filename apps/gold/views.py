from django.shortcuts import render, redirect
import random
from datetime import datetime

def index(request):
	if 'gold' in request.session:
		pass
	else:
		request.session['gold'] = 0
	return render(request, 'gold/index.html')

def process_money(request):
	if 'activities' not in request.session:
		request.session['activities'] = []
	if request.POST['action'] == 'farm':
		farm_gold = random.randrange(10,21)
		request.session['gold'] += farm_gold
		message = "Earned "+str(farm_gold)+" gold coins from the farm!"+str(datetime.now().strftime("%Y-%m-%d %H:%M"))
	elif request.POST['action'] == 'cave':
		cave_gold = random.randrange(5,11)
		request.session['gold'] += cave_gold
		message = "Earned "+str(cave_gold)+" gold coins from the cave!"+str(datetime.now().strftime("%Y-%m-%d %H:%M"))
	elif request.POST['action'] == 'house':
		house_gold = random.randrange(2,5)
		request.session['gold'] += house_gold
		message = "Earned "+str(house_gold)+" gold coins from the house!"+str(datetime.now().strftime("%Y-%m-%d %H:%M"))
	elif request.POST['action'] == 'casino':
		casino_gold = random.randrange(-50,50)
		request.session['gold'] += casino_gold
		if casino_gold >= 0:
			message = "Entered a casino and won "+str(casino_gold)+" gold coins! "+str(datetime.now().strftime("%Y-%m-%d %H:%M"))
		else: 
			message = "Entered a casino and lost "+str(casino_gold)+" gold coins! "+str(datetime.now().strftime("%Y-%m-%d %H:%M"))
	request.session['activities'] = [message] + request.session['activities']
	return redirect('/')
