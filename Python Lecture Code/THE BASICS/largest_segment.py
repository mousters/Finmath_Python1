
def largestSegment(radius, numberOfSegments):
    #initializing
    threshold=0.0001
    pi=3.14159265359

    '''
    OPTIMIZATION, NOT THE CENTRAL PART OF THE CODE
    circle_num=len(radius)
    #check unique case: when there is only one circle in the input
    if(circle_num<1):
        assert False
    if(circle_num==1):
        return radius[0]*radius[0]*pi/circle_num
    
    #determine the number of circles needed
    cnt=dict(zip(radius, [0 for i in range(circle_num)]))
    area=dict()
    #get basic info about the area and number of each circle
    for i in range(circle_num):
        area[radius[i]]=radius[i] * radius[i] * pi
        cnt[radius[i]]+=1
    radius_temp=list(cnt.keys())
    radius_temp.sort(reverse=True)
    #radius temp stores the circle from larges to smallest
    # and cnt stores the number of circles with unique radius

    #the reasoning behind this step is that
    #if after dividing the first a few largest circles by number of segments
    #the area of each segment is greater than any of the remaining circles,
    #we only need to iterate throw these large circles rather than include
    #all of the circles in the algorithm
    #in such a way, memory is saved and potentially faster

    #usage is how many circles do we need
    #increase the number (unique radius) we need until
    #after dividing the selected circles, the area is greater than the rest
    usage=1
    for i in range(len(radius_temp)-1):
        large_circles_divided_by_num=area[radius_temp[i]]*cnt[radius_temp[i]]/numberOfSegments
        smaller_cirles=area[radius_temp[i+1]]
        if(large_circles_divided_by_num<smaller_cirles):
            usage+=1
        else:
            break
    new_areas = []
    for i in range(usage):
        for j in range(cnt[radius_temp[i]]):
            new_areas.append(area[radius_temp[i]])
    #new areas reduces the number of circles needed
    '''

    new_areas=[]
    for i in radius:
        new_areas.append(i**2 * pi)
    base=min(new_areas)/numberOfSegments
    cap=max(new_areas)
    new_cir_num=len(new_areas)

    while(cap-base>threshold):
        #start with the middle between largest (cap) and smallest area (base)
        mid=(cap+base)/2
        fit_num=0
        for i in range(new_cir_num):
            #test if this middle area can be fitted into every circle
            fit_num+=int(new_areas[i]/mid)
        if (fit_num<numberOfSegments):
            #if the number fitted smaller than the number of segments, meaning it is too large
            #the middle area becomes the new cap
            cap=mid
        else:
            #vice versa
            #every circle can fit this much, so mid becomes the new base
            base=mid
    #the largest area
    largest_area=round(mid,4)
    return largest_area


if __name__=='__main__':
    radius=[1,1,1,2,2,3]
    numberOfSegments=6
    print(largestSegment(radius,numberOfSegments))

