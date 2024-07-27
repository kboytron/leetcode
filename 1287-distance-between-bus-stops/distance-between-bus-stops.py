class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        if start > destination:
            start,destination = destination, start

        clockwise = sum(distance[start:destination])

        total = sum(distance)

        counter = total - clockwise

        return min(clockwise, counter)
        