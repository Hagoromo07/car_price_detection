MODELS_LIST = [
    'km',
    'Gears',
    'age',
    'Previous_Owners',
    'hp_kW',
    'Inspection_new',
    'Displacement_cc',
    'Weight_kg',
    'cons_comb',
    'Air conditioning',
    'Air suspension',
    'Armrest',
    'Automatic climate control',
    'Auxiliary heating',
    'Cruise control',
    'Electric Starter',
    'Electric tailgate',
    'Electrical side mirrors',
    'Electrically adjustable seats',
    'Electrically heated windshield',
    'Heads-up display',
    'Heated steering wheel',
    'Hill Holder',
    'Keyless central door lock',
    'Leather seats',
    'Leather steering wheel',
    'Light sensor',
    'Lumbar support',
    'Massage seats',
    'Multi-function steering wheel',
    'Navigation system',
    'Panorama roof',
    'Park Distance Control',
    'Parking assist system camera',
    'Parking assist system self-steering',
    'Parking assist system sensors front',
    'Parking assist system sensors rear',
    'Power windows',
    'Rain sensor',
    'Seat heating',
    'Seat ventilation',
    'Split rear seats',
    'Start-stop system',
    'Sunroof',
    'Tinted windows',
    'Wind deflector',
    'Windshield',
    'Bluetooth',
    'CD player',
    'Digital radio',
    'Hands-free equipment',
    'MP3',
    'On-board computer',
    'Radio',
    'Sound system',
    'Television',
    'USB',
    'Alloy wheels',
    'Cab or rented Car',
    'Catalytic Converter',
    'Handicapped enabled',
    'Right hand drive',
    'Roof rack',
    'Shift paddles',
    'Ski bag',
    'Sliding door',
    'Sport package',
    'Sport seats',
    'Sport suspension',
    'Touch screen',
    'Trailer hitch',
    'Tuned car',
    'Voice Control',
    'Winter tyres',
    'ABS',
    'Adaptive Cruise Control',
    'Adaptive headlights',
    'Alarm system',
    'Blind spot monitor',
    'Central door lock',
    'Central door lock with remote control',
    'Daytime running lights',
    'Driver drowsiness detection',
    'Driver-side airbag',
    'Electronic stability control',
    'Emergency brake assistant',
    'Emergency system',
    'Fog lights',
    'Head airbag',
    'Immobilizer',
    'Isofix',
    'LED Daytime Running Lights',
    'LED Headlights',
    'Lane departure warning system',
    'Night view assist',
    'Passenger-side airbag',
    'Power steering',
    'Rear airbag',
    'Side airbag',
    'Tire pressure monitoring system',
    'Traction control',
    'Traffic sign recognition',
    'Xenon headlights',
    'Demonstration',
    "Employee's car",
    'New',
    'Pre-registered',
    'Used',
    'Audi A1',
    'Audi A2',
    'Audi A3',
    'Opel Astra',
    'Opel Corsa',
    'Opel Insignia',
    'Renault Clio',
    'Renault Duster',
    'Renault Espace',
    'Compact',
    'Convertible',
    'Coupe',
    'Off-Road',
    'Sedans',
    'Station wagon',
    'Transporter',
    'Van',
    'Price negotiable',
    'VAT deductible',
    'Benzine',
    'Diesel',
    'Electric',
    'LPG/CNG',
    'Metallic',
    'Perl effect',
    'Uni/basic',
    'Cloth',
    'Part/Full Leather',
    'Automatic',
    'Manual',
    'Semi-automatic',
    '4WD',
    'front',
    'rear']


def create_input_dict():
    """
    Create a dictionary with default values for the model input.
    The keys are the model columns and the values are set to 0.
    If the user provides specific values, those keys are set to 1.
    """
    # Initialize input_dict with default values (0)
    input_dict = {col: 0 for col in MODELS_LIST}
    return input_dict


def get_comfort_convenience():
    return {
        'comfort_convenience': [
            'Leather seats', 'Navigation system', 'Electrically heated windshield', 'Panorama roof',
            'Air conditioning', 'Start-stop system', 'Heads-up display', 'Tinted windows',
            'Seat heating', 'Hill Holder', 'Park Distance Control', 'Electric Starter',
            'Lumbar support', 'Light sensor', 'Sunroof', 'Electric tailgate',
            'Heated steering wheel', 'Power windows', 'Parking assist system sensors rear',
            'Automatic climate control', 'Keyless central door lock', 'Electrical side mirrors',
            'Split rear seats', 'Parking assist system sensors front', 'Auxiliary heating',
            'Wind deflector', 'Leather steering wheel', 'Electrically adjustable seats',
            'Parking assist system self-steering', 'Cruise control', 'Armrest', 'Air suspension',
            'Rain sensor', 'Windshield', 'Multi-function steering wheel',
            'Parking assist system camera', 'Seat ventilation', 'Massage seats'
        ]
    }


def get_entertainment_media():
    return {
        'entertainment_media': [
            'Bluetooth', 'Sound system', 'Radio', 'Television', 'USB', 'On-board computer',
            'CD player', 'Digital radio', 'MP3', 'Hands-free equipment'
        ]
    }


def get_extras():
    return {
        'extras': [
            'Sport seats', 'Sport suspension', 'Cab or rented Car', 'Right hand drive', 'Touch screen',
            'Catalytic Converter', 'Handicapped enabled', 'Sport package', 'Tuned car', 'Winter tyres',
            'Voice Control', 'Trailer hitch', 'Roof rack', 'Sliding door', 'Alloy wheels', 'Ski bag',
            'Shift paddles'
        ]
    }


def get_safety_security():
    return {
        'safety_security': [
            'Fog lights', 'Driver drowsiness detection', 'Night view assist', 'Head airbag',
            'Central door lock with remote control', 'Electronic stability control', 'Alarm system',
            'Emergency system', 'Xenon headlights', 'Power steering', 'LED Daytime Running Lights',
            'Driver-side airbag', 'ABS', 'Traction control', 'Emergency brake assistant', 'Side airbag',
            'Adaptive Cruise Control', 'Central door lock', 'LED Headlights', 'Blind spot monitor',
            'Immobilizer', 'Daytime running lights', 'Adaptive headlights', 'Traffic sign recognition',
            'Rear airbag', 'Isofix', 'Lane departure warning system', 'Passenger-side airbag',
            'Tire pressure monitoring system'
        ]
    }


def get_vehicle_specifications():
    return {
        'fuel': ['Diesel', 'Benzine', 'LPG/CNG', 'Electric'],
        'type': ['Used', "Employee's car", 'New', 'Demonstration', 'Pre-registered'],
        'body_type': ['Sedans', 'Station wagon', 'Compact', 'Coupe', 'Van', 'Off-Road', 'Convertible', 'Transporter'],
        'make_model': ['Audi A1', 'Audi A2', 'Audi A3', 'Opel Astra', 'Opel Corsa', 'Opel Insignia', 'Renault Clio',
                       'Renault Duster', 'Renault Espace'],
        'pain_type': ['Metallic', 'Uni/basic', 'Perl effect'],
        'upholstery_type': ['Cloth', 'Part/Full Leather'],
        'gearing_type': ['Automatic', 'Manual', 'Semi-automatic'],
        'displacement_cc': 0,
        'weight_kg': 0,
        'drive_chain': ['front', '4WD', 'rear'],
        'cons_comb': [3.8, 5.6, 4.1, 3.5, 3.7, 4.2, 4.0, 4.9, 4.5, 4.4, 4.3, 3.0, 3.6, 3.4, 3.9, 5.1, 5.2, 4.6, 4.8,
                      5.0, 5.8, 4.7, 4.55, 6.0, 5.9, 4.300000000000002, 5.3, 3.65, 5.5, 3.3, 3.95, 3.2, 6.6, 8.3, 6.5,
                      7.1, 8.1, 5.4, 6.4, 6.7, 6.2, 7.3, 6.3, 5.7, 6.1, 6.8, 7.5, 7.4, 5.45, 7.8, 3.1, 6.9, 7.0, 7.2,
                      8.0, 9.1, 8.6, 8.7, 7.9, 5.15, 3.45, 7.6],
        'age': 0,
        'gears': [7.0, 6.0, 5.0, 8.0],
        'km': 0
    }


def get_convenience_entertainment():
    # Optionally merge all parts if needed
    return {
        **get_comfort_convenience(),
        **get_entertainment_media(),
        **get_extras(),
        **get_safety_security(),
        **get_vehicle_specifications()
    }


MODEL_COLUMNS = create_input_dict()
FORMAT_COLUMNS = get_convenience_entertainment()
