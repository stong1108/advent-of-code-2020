import re

with open('input.txt') as f:
    lines = map(lambda x: x.strip(), f.readlines())

pattern = re.compile(r'(byr|iyr|eyr|hgt|hcl|ecl|pid|cid):')
passports = []

curr_passport = ''
for l in lines:
    if l:
        curr_passport = ' '.join([curr_passport, l]).lstrip()
    else:
        passports.append(curr_passport)
        curr_passport = ''
passports.append(curr_passport)


# Part 1
required = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])

n = 0
for passport in passports:
    fields = set(re.findall(pattern, passport))
    if 'cid' in fields:
        fields.remove('cid')
    if required == fields:
        n += 1

print(n)

# Part 2
# pattern = re.compile(r'((?:byr|iyr|eyr|hgt|hcl|ecl|pid|cid):\S+)')
required = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])

d_validations = {'byr': {'pattern': r'\d{4}',
                        'bounds': (1920, 2002)
                        },
                'iyr': {'pattern': r'\d{4}',
                        'bounds': (2010, 2020)
                        },
                'eyr': {'pattern': r'\d{4}',
                        'bounds': (2020, 2030)
                        },
                'hgt': {'pattern': r'(?:\d{3}cm)|(?:\d{2}in)',
                        'bounds': {'cm': (150, 193),
                                    'in': (59, 76)
                                }
                        },
                'hcl': {'pattern': r'#[0-9a-f]{6}'},
                'ecl': {'pattern': r'(?:amb|blu|brn|gry|grn|hzl|oth)'},
                'pid': {'pattern': r'^[0-9]{9}$'}
                }

valid_pattern = re.compile(r'(byr|iyr|eyr|hgt|hcl|ecl|pid|cid):')
valid_passports = []

for passport in passports:
    fields = set(re.findall(valid_pattern, passport))
    if 'cid' in fields:
        fields.remove('cid')
    if required == fields:
        valid_passports.append(passport)

parsing_pattern = re.compile(r'((?:byr|iyr|eyr|hgt|hcl|ecl|pid):\S+)')

n = 0
for vp in valid_passports:
    l_fields = re.findall(parsing_pattern, vp)
    valid_fields = True
    for field in l_fields:
        name, value = field.split(':')
        validations = d_validations[name]
        matched_pattern = re.findall(validations['pattern'], value)
        if len(matched_pattern) != 1:
            valid_fields = False
            break
        bounds = validations.get('bounds', None)
        if type(bounds) == tuple:
            value = int(value)
            if value < bounds[0] or value > bounds[1]:
                valid_fields = False
                break
        elif type(bounds) == dict:
            actual_bounds = bounds[value[-2:]]
            value = int(value[:-2])
            if value < actual_bounds[0] or value > actual_bounds[1]:
                valid_fields = False
                break
    if valid_fields:
        n += 1

print(n)
