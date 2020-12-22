with open('input.txt') as f:
    inputs = list(map(lambda x: x.strip(), f.readlines()))

earliest = int(inputs[0])
buses = [int(bus_id) for bus_id in inputs[1].split(',') if bus_id.isnumeric()]

# Part 1
min_wait = earliest
desired_bus = None

for bus in buses:
    mod = earliest % bus
    if mod == 0:
        waittime = 0
    else:
        waittime = bus - mod
    if waittime < min_wait:
        min_wait = waittime
        desired_bus = bus

print(min_wait * desired_bus)

# Part 2
n = int(100000000000000/buses[0])

d_bus_diffs = dict((int(bus_id), i) for i, bus_id in enumerate(inputs[1].split(',')) if bus_id.isnumeric())

done = False

while not done:
    t = n * buses[0]
    matches = 0
    for k,v in d_bus_diffs.items():
        if k == 7:
            matches += 1
            continue
        if v != k - t % k:
            n += 1
            break
        else:
            matches += 1
    if matches == len(d_bus_diffs):
        done = True
        print(t)

'''
import com.expedia.www.sem.ad.copy.service.vulcan2.templates.eta.hotel.pt.definitions.ValueConstraints.hasFreeBreakfast
import com.expedia.www.sem.ad.copy.service.vulcan2.templates.eta.hotel.pt.definitions.ValueConstraints.hasBreakfast
import com.expedia.www.sem.ad.copy.service.vulcan2.templates.eta.hotel.pt.definitions.ValueConstraints.hasViewOcean
import com.expedia.www.sem.ad.copy.service.vulcan2.templates.eta.hotel.pt.definitions.ValueConstraints.hasView
import com.expedia.www.sem.ad.copy.service.vulcan2.templates.eta.hotel.pt.definitions.ValueConstraints.hasPatio

val descriptionG2 = variants(
  variant({ "Hotel with free breakfast, clean rooms, and relaxing atmosphere." }, hasFreeBreakfast),
  variant({ "Hotel with free breakfast, friendly staff, etc? Awesome." }, hasFreeBreakfast),
  variant({ "${starRating()}-star Hotel with free breakfast included." }, hasFreeBreakfast),
  variant({ "Hotel with breakfast, clean rooms, and relaxing atmosphere." }, hasBreakfast),
  variant({ "Hotel with breakfast, friendly staff, etc? Awesome." }, hasBreakfast),
  variant({ "${hotelName()} has a beautiful patio and stunning views." }, hasPatio, hasView),
  variant({ "${hotelName()} has an incredible view and private beach." }, hasView, hasBeachPrivate),
  variant({ "${starRating()}-star ${hotelName()} with amazing ocean view." }, hasViewOcean),
  variant({ "${starRating()}-star ${hotelName()} in nice location with superb view." }, hasView),
  variant({ "${starRating()}-star ${hotelName()} with phenomenal view." }, hasView),
  variant({ "The view from ${hotelName()} is unparalleled." }, hasView),
  variant({ "Hotel with full-service spa, relaxing vacation." }, hasSpa),
  variant({ "${hotelName()} has a wonderful spa." }, hasSpa)
).default("Plan Your Next Trip with Expedia.")
'''
