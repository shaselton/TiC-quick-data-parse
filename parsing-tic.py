import json

# negotiated rates for the NEONATES, DIED OR TRANSFERRED TO ANOTHER ACUTE CARE FACILITY service
with open('testfile.json') as fid:
    negotiation_data = json.load(fid)
    
    
# all of the defined provider references at the top of the file.
with open('provider_reference.json') as fid:
    provider_references = json.load(fid)
    
#total provider references in the file.
len(provider_references["provider_references"]) # 9059


prices = []

#find each provider reference used in the negotiated rate for the service.
for negotiated_rates in negotiation_data['negotiated_rates']:
    temp_providers = []
    for providers in provider_references['provider_references']:
        if providers['provider_group_id'] in negotiated_rates['provider_references']:
            temp_providers = temp_providers + providers['provider_groups']
    
    if len(temp_providers) > 0:
        prices.append([temp_providers, {"negotiated_rate": negotiated_rates['negotiated_prices'][0]['negotiated_rate']}])
prices
