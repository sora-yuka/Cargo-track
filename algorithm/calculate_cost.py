def equipment(equip):
    if(equip=='Dry'):
        return 500
    if(equip=='Flatbed'):
        return 200
    if(equip=='Reefer'):
        return 1000
    if(equip=='Step Deck'):
        return 300
    if(equip=='Double Drop'):
        return 300
    if(equip=='Tanker'):
        return 900
    return 0

def rating(carrier_rating):
    return 1.0+(carrier_rating/100.0)

def pricing (distance, average_gas_cost, market_rates, weight, volume, is_urgent, special_handling, route_type, equipment_needed,carrier_rating):
    total_price=3000 #стартовая цена
    #Factors
    weight_factor=0.05 #per lbs
    volume_factor=0.01 #per foot^3
    urgency_factor=1.20 #+20%
    special_handling_factor=1.15 #+15%
    urban_route_factor=1.10 #+10%
    rural_route_factor=0.95 #-5%


    #gas price
    distance_km = 1.60934*distance
    gas_needed = (33.8*distance_km)/(1000*0.85*2.3) #https://hc-russia.ru/poleznaya-informatsiya/81-universalnyj-raschet-raskhoda-topliva-dlya-dizelnogo-vilochnogo-pogruzchika

    total_price+=(average_gas_cost+market_rates)*gas_needed
    
    #weight & volume
    total_price+=(weight*weight_factor+volume*volume_factor)

    #other 
    total_price+=equipment(equipment_needed)
    if is_urgent:
        total_price*=urgency_factor
    if special_handling:
        total_price*=special_handling_factor
    if route_type=='urban':
        total_price*=urban_route_factor
    elif route_type=='rural':
        total_price*=rural_route_factor
    total_price*=rating(carrier_rating)
    return total_price