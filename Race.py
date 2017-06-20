### Enable logging ###
StartDetailedLoging()
StartUserLog()

### Get the starting lane ###
WaitForSeconds(2.0)
#startLane = round(CurrentTrackPosition())
#AimForLane(startLane)
AimForLane(CurrentTrackPosition())
### Start of the race ###
WaitForGo()
Lap=0
# Starting straight
#AimForLane(startLane)
Speed(100)
AimForLane(CurrentTrackPosition())
#AimForLane(0)
WaitForSeconds(0.2)
### Racing until terminated ###
while Globals.running:
	WaitForWaypoint(2)
	# First corner of the race
	# Drive in the center until turn 2
	AimForLane(-2.5)
	WaitForWaypoint(4)
	AimForLane(-1.75)
	WaitForWaypoint(5)
	# Drive on the middle of the inner blue lane
	# until the back straight
	AimForLane(-1.0)
	WaitForWaypoint(6)
	# Move towards the center of the track
	# so we do not try and turn too sharply
	AimForLane(-2)
	Lap = Lap+1;
	#WaitForSeconds(0.5)
	# Drive on the middle of the outer blue lane
	# until the start / finish line
	WaitForWaypoint(1)
	if Lap >= 3:
                break;

### Continue racing for a few seconds ###
#WaitForSeconds(4)
for slowing in range(99, -1, -1):
	Speed(slowing)
	WaitForSeconds(0.01)
### End of the race ###
EndDetailedLog()
EndUserLog()
FinishRace()
