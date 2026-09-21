---
title: "RCorp Rail"
order: 9
section: "Transport Infrastructure"
description: "RCorp Rail is Redstoneworld's latest transport network. It connects all major landmarks and sectors in Chapter 7 using distinct highways and pods."
image: "/wiki/assets/images/rcrailbanner.webp"
image_alt: "RCorp Rail track and pods at the Global Control RTC Station."
last_modified: "2026-09-18T04:02:30Z"
contributor: "Ijd710"
infobox: {"Started": "July 5th, 2023", "Project Directors": "Mr. Ij, Mr. Void, LLucas, EzraThunder, SomeYTguyFor1", "Completed":"March 18th, 2026", "Type": "Global Infrastructure"}
published: true
---

RCorp Rail is the latest transportation system on Redstoneworld. Designed to be both a companion and successor to the old {% include wiki-link.html title="U1" %} system, RCorp Rail uses two player pods, a fast speed, interconnected rails, and a subscription model to move users around efficiently and economically. 

RCorp Rail was opened live on March 18th, 2026, with the release of the [RCorp Rail Trailer](https://youtu.be/1IB7DyI7OLE)

It was first proposed in 2023 during {% include wiki-link.html title="Chapter 6" %} by Mr. Void.

Note that a video deep dive of RCorp Rail is available as <a href="/wiki/ijs-devlogs/#devlog34">Devlog 34</a>, it goes into detail on all stations as well as the code.

It was also the first project where the GitHub datapack system was used for collaboration, followed by the {% include wiki-link.html title="RTC Reactor" %}.

## Subscription

{% include wiki-image.html file="/wiki/assets/images/rcrailsub.webp" caption="The subscription checking commands under the Dos Village RCorp Rail Station entrance" side="left" %}
While U1 worked using prepaid tickets (at 4 per gold ingot) RCorp Rail uses a monthly subscription. This is done through the day counter, every 30 day counter increments will increment the month counter by one. The standard price is 2 emeralds per month, however for RCorp Clearance 1 it is 1 emerald per month, 2 becomes 1 diamond per month, and 3 or above is completely free. Users can register their RCorp Clearance at the {% include wiki-link.html title="Founding Island Bunker" %}'s Security Center with an appropriate staff card. 

### Signing up

Subscriptions are activated at an entrance to any public [Station](#stations). The checkpoint pressure plate simply checks if the user above is subscribed, opens the gate if true, and signs them up if not. We decided to make it work this way to save lag that using interactive sign up stations would have caused. Triggering a sign up sets the users 'rcrailpay' scoreboard based on their cost, then creates a marker under Spawn tied to the users redstoneworldID. This keeps track of months even while players are offline, then the subscription months are checked and paid out if needed upon players rejoining. Currently, it pays using the EssentialsX balance of the user, but this will be switched to scoreboard for the world download.

### Cancelling

The RCorp Rail subscription can only be removed at the Tower 3.0 Station, and also must be cancelled to switch to a new cost tier. Cancelling can be globally disabled at the RTC RCorp Rail [Admin Room](#admin-controls) and requires the player to complete a small maze first.

## Rail and Highway

{% include wiki-image.html file="/redstoneworld-org/assets/images/rcorp-rail-detail.webp" caption="The map from RCorp Rail First Run, missing the Reborn X Museum" side="right" %}

The rail setup for RCorp Rail is actually quite simple, it has a cosmetic shell with different kinds of deepslate but the reality of it is vanilla rails three blocks below the reinforced deepslate top. Interchanges and stations use generic redstone torch rail switchers.

To zoom out the RCorp Rail is a large interconnected network featuring regular routes, loops, bypasses, and spurs. The Interstate Highway system of the U.S.A. provided lots of inspiration. All rails were built by Ij, but there was lots of contributions by other builders to add the stairs and other elements, the tools Axiom and WorldEdit were also of great assistance.

### Highway Details

#### RW-10
RW-10 is the far northern east-west route. It starts at the restricted {% include wiki-link.html title="Testing Sector" %} and heads north then east. At the 4 way interchange it turns north to then go east towards the {% include wiki-link.html title="Forgotten Isle" %} It then heads far east and then south to approach and terminate at the {% include wiki-link.html title="Blakewood Forest Rakegame" %}.
#### RW-210
RW-210 is the Site Omega-5 (Forgotten Isle) emergency bypass. It quickly takes an unauthorized rider out of the zone to then end back at RW-10 after.
#### RW-11
RW-11 is the other end of the Testing Sector station. It heads south before turning east and terminating at an interchange with RW-13/RW-20 at the {% include wiki-link.html title="Redstone Theme Park" %}. This was the last piece of track added in the original development of RCorp Rail.
#### RW-12
RW-12 is the central northern east-west route. It starts heading east from the 4 way interchange then heads south to hit the northern spur for the {% include wiki-link.html title="Main Redstone Bunker" %}. It continues east where it has another interchange for the spur to the {% include wiki-link.html title="Rakeport" %}. Continuing east and now very high above the FI Jungle, it has a major interchange with RW-15 and continues southeast to {% include wiki-link.html title="Global Control" %}. It terminates at the East Village station.
#### RW-112
RW-112 is a spur continuing south of East Village to terminate at RW-20 for the interchange for Blakewood Forest.
#### RW-312
RW-312 is a spur that wraps under RW-12 to serve the Rakeport station.
#### RW-512
RW-512 is a spur that runs southwest to serve the north end of the Main Bunker station.
#### RW-13
RW-13 is the western north-south route. It starts heading south from the 4 way interchange, where it has the {% include wiki-link.html title="Redstone Cruise Ship" %} Station. South of that is an interchange with RW-113 where it continues into the Theme Park, going through the Pirate Island while splitting and rejoining with RW-213. It terminates briefly after next to the Waterpark with an interchange with RW-11 and RW-20.
#### RW-113
RW-113 is a spur that heads east from an interchange between the Cruise Ship and Theme Park to connect to RW-215.
#### RW-213
RW-213 serves the Theme Park station and wraps through the Pirate Island to meet back with RW-13.
#### RW-15
RW-15 is the north-south route for western {% include wiki-link.html title="Founding Island" %}. It begins at the interchange with RW-12 above the FI Jungle, then heads south to the Spawn station. Directly south it has an interchange with RW-215 then enters the {% include wiki-link.html title="Founding Island Bunker" %} splitting and rejoining with RW-415. It exits the FI Bunker then heads east to terminate at an interchange with RW-17 at the [Redstone Tower Complex](/wiki/redstone-tower-complex-rtc-sector/). 
#### RW-215 / RW-215 CCW
Known as the Dos Loop, RW-215 heads west from the FI Bunker and begins its one way counterclockwise loop. It first has an interchange with RW-215 CCW which completes the shorter loop then an interchange with RW-315 for the south side of the Main Bunker Station. Immediately after is the interchange with RW-113. It then heads south into the Dos Mountains for the {% include wiki-link.html title="Dos Village" %} station. It moves east then north to an interchange with RW-120 for the Villa and immediately after the SMP Base Station. After that going north has RW-215 CCW which reenters the shorter loop, while RW-215 continues east to the Gerudo Desert station, and then back to the FI Bunker.
#### RW-315
RW-315 is a spur that runs north to serve the south end of the Main Bunker station.
#### RW-415
RW-415 serves the FI Bunker station and was also the first segment of RCorp Rail made. Fully underground.
#### RW-17
{% include wiki-image.html file="/wiki/assets/images/rcrailcrazy.webp" caption="The Crazy Interchange as it appears after Reborn X. RW-17 runs straight north-south, RW-15 is seen on the west, RW-217 going into the RTC in northeast, and RW-317 serving the museum in the southwest." side="left" %}
RW-17 is the north-south route for the Redstone Tower Complex. It begins at the interchange with RW-12 at Global control, then heads south under the bridge to {% include wiki-link.html title="Tower 3.0" %} where it splits and rejoins as RW-217. Immediately after is the nicknamed "Crazy Interchange" where RW-17, RW-217, RW-15, and RW-317 for the Reborn X Museum all meet. RW-17 continues southeast and terminates at RW-20 near {% include wiki-link.html title="Tavish Town" %}.
#### RW-217
RW-217 is a loop that goes through the lower levels of Tower 3.0 to serve one of the busiest stations.
#### RW-317
RW-317 is a spur from that runs northwest to serve the Reborn X Museum and uses RW-15 to terminate. This is the most recent piece of track as of Reborn X.
#### RW-20
RW-20 is the far southern east-west route. It starts east of the interchange with RW-11 and RW-13 at the Waterpark. It heads east, wrapping around the south Dos Mountains where it has an interchange with RW-120. It continues to its Tavish Town Station and then the interchange with RW-17. Afterwards there is a brief north stretch to the interchange with RW-112 where it then shoots east for the Blakewood Forest while wrapping around the barrier. It terminates just north of the Blakewood Forest station.
#### RW-120
RW-120 is a spur that runs northwest from RW-20 to serve the Villa station, then terminating at the Dos Loop RW-215.
#### RW-220
RW-220 is the Blakewood Forest emergency bypass. It quickly takes an unauthorized rider out of the zone to then end back at RW-20.

## Pod mechanics

The RCorp rail pod uses a myriad of entities, including block & item displays, a pig and famously, a tadpole mounted on a minecart. Below the main highway there is an ordinary minecart track, and therefore the default speed of the RCorp rail pod is 0.4 blocks/tick (8 blocks/sec at 20 TPS). However, on straight sections, the RCorp pod has the ability to accelerate to a much higher speed, allowing it to traverse the world faster than a U1 cart. Each full RCorp Rail pod is 67 entities (65 ghost). All pod mechanics were designed and implemented by Ij and LLucas in early 2026. All RCorp pods have their own unique ID which is used to link up rotations and seats. This is stored in `redstoneworldID`, the next ID is stored in `#rcrailtrip redstoneworldID`

### Teleportation

Every tick, the minecart on which the RCorp pod is mounted summons a marker. This marker recursively checks ahead of itself until it encounters a block that is not a powered rail. Hence, it is able to determine the amount of blocks there are remaining on a straight path until the rail either goes up, down, or curves. Based on the amount of blocks, the RCorp rail pod will select an appropriate speed and teleport every tick in order to achieve that speed. On perfectly straight paths, the minecart has the ability to teleport 2.1 blocks every tick (and hence reach a speed of 2.5 blocks per tick or 50 blocks per second, since motion is still applied to the minecart after teleportation).

<div class="wiki-table-wrap">
<table>
<caption>RCorp rail straight path requirements and speed values</caption>
<thead><tr><th>Number of blocks</th><th>Additional speed (b/t)</th><th>Additional speed (b/s)</th><th>Total speed (b/t)</th><th>Total speed (b/s)</th></tr></thead>
<tbody>
<tr><td>0 blocks (Default)</td><td>0.0 blocks per tick</td><td>0 blocks per sec</td><td>0.4 blocks per tick</td><td>8 blocks per sec</td></tr>
<tr><td>8 blocks (Boost I)</td><td>0.7 blocks per tick</td><td>14 blocks per sec</td><td>1.1 blocks per tick</td><td>22 blocks per sec</td></tr>
<tr><td>16 blocks (Boost II)</td><td>1.1 blocks per tick</td><td>22 blocks per sec</td><td>1.5 blocks per tick</td><td>30 blocks per sec</td></tr>
<tr><td>32 blocks (Boost III)</td><td>1.7 blocks per tick</td><td>34 blocks per sec</td><td>2.1 blocks per tick</td><td>42 blocks per sec</td></tr>
<tr><td>48 blocks (Boost IV)</td><td>2.1 blocks per tick</td><td>42 blocks per sec</td><td>2.5 blocks per tick</td><td>50 blocks per sec</td></tr>
</tbody>
</table>
</div>

#### Speeding up

Speeding up does not simply use the straight path requirement in order to determine the speed at that instant. Rather, it has a 12 game tick cooldown in order to make the acceleration more smooth. The target speed is selected purely based off of the straight path requirement, then that speed is reached via acceleration every 12 game ticks. Every single time the pod accelerates, it plays the `minecraft:block.beacon.activate` (beacon activation) sound with pitch 2.

#### Slowing down

Conversely, a cooldown is not required for the slowing down mechanic, as the straight path distance drops predictably and gradually as the pod approaches a portion of the rail which is not fully straight. Hence, there is no cooldown. Upon slowing down, the pod plays the `minecraft:block.beacon.deactivate` (beacon de-activation) sound with pitch 2.

### Speedometer

During an RCorp rail ride, the speed of the pod is displayed above the actionbar in metres per second and in kilometres per hour.

Every 10 ticks, the speedometer first takes the x and z position of the minecart (scaled by a factor of 1000) and stores them in a scoreboard. One tick later, it does the same, storing the result in a different scoreboard value. Once this finishes, it finds the difference between the two values (which is in 1/1000ths of a block), and sets a temporary "speed" value to the speed on the x axis. If the speed on the z axis exceeds that of the x axis, it sets the temporary "speed" value to that of the z axis. After this, if the x and z values match, the speed value is multiplied by 1.414 (approximately the square root of 2) in order to account for diagonal rails.

After this value is computed, it is multiplied by the TPS value on the TPS system, which is in ticks per 100 seconds (2000 is equivalent to 20.00 TPS). This allows the speed to be lag compensated (i.e. at normal minecart speed at 10 TPS, the speedometer would display 4.0 blocks per second). In order for this value to be useable, it is processed via division.

For the value in kilometres per hour, the value is copied. Then, 1389 is added to the value (for rounding behaviour on the division rather than flooring), then divided by 2778, which yields the values in 1/10ths of a kilometre per hour. This value is later formatted on the action bar.

For the value in metres per second, a similar procedure is executed, instead adding 5000 to the value and dividing by 10000 to yield the value in 1/10ths of a metre per second.

As a bonus feature of the speedometer code, a subtitle is displayed to the user showing their current set destination.

### Movement

{% include wiki-image.html file="/wiki/assets/images/rcrailpod.webp" caption="The RCorp Rail pod prototypes, as seen from the Testing Sector. Left is the first block display and right the original build." side="right" %}
RCorp Rail pods are primarily physically moved through the rcraildrive minecart at the bottom riding the internal highway. See [Teleportation](#teleportation). However, the minecart rotation does not directly apply to any other entities, even the ones direct passengers of it, and matching rotation data every tick caused significant TPS lag, so this required some more ingenuity. The seat movement is handled every tick and cannot be interpolated smoothly, requiring separate commands depending on the current speed. Since there are a lot more entities for the pod rotation, that is ran every 3 ticks instead. The rotation is only applied to all entities if the rotation of the first armor stand is detected to be different from the bottom minecart. 

Additionally, the pods are constantly inspected for player counts for regular pods and movement checks for ghost pods. Failure to reach these conditions start a timer that will automatically kill the pods after a certain time. Ghost pods have another automatic kill that triggers if they are anywhere too close to any other pod.

## Routing mechanics

RCorp Rail pods are spawned at [Stations](#stations) and are given a destination. The pods will then follow the rails to that destination, using the shortest path possible. 

### Interchanges

Under each RCorp Rail junction is a commandblock that is reading certain scoreboard info from the rcraildrive minecart under the pod and switching a rail to put the pod on the correct [rail](#highway-details). Specifically we are looking at its score of `rcsid`, `rcsx`, and `rcsz`, referring to the station's ID, RCx, and RCz grid coordinates respectively. Each junction was intelligently programmed to pick fast routes, keeping in mind that RCorp Rail highways are not a perfect grid and have routes that twist and turn. Our coordinates RCx and RCz are not the same as the world coordinates, they are our own grid system that is used to make the routing smart. The most accurate coordinate information is stored in our [RCorp Rail spreadsheet](https://docs.google.com/spreadsheets/d/1L-LnMNDEWJ6JDecYKffRuZo3hcXt2bSP2P0uQazk9oo/view), but the table below is up to date as of September 2026. 

<div class="wiki-table-wrap">
<table>
<caption>RCorp Rail station IDs and grid coordinates</caption>
<thead><tr><th>Station Name</th><th>Station ID (rcsid)</th><th>X Coordinate (rcsx)</th><th>Z Coordinate (rcsz)</th><th>Station Tellraw ID (rcrailtrig)</th></tr></thead>
<tbody>
<tr><td>Testing Sector</td><td>0</td><td>0</td><td>1</td><td>15</td></tr>
<tr><td>Redstone Theme Park</td><td>1</td><td>1</td><td>14</td><td>1</td></tr>
<tr><td>Redstone Cruise Ship</td><td>2</td><td>2</td><td>6</td><td>2</td></tr>
<tr><td>Dos Village</td><td>3</td><td>3</td><td>13</td><td>3</td></tr>
<tr><td>Main Bunker</td><td>4</td><td>4</td><td>3</td><td>4</td></tr>
<tr><td>Dos SMP Base</td><td>5</td><td>5</td><td>12</td><td>5</td></tr>
<tr><td>Gerudo Desert</td><td>6</td><td>6</td><td>9</td><td>6</td></tr>
<tr><td>Villa</td><td>7</td><td>7</td><td>14</td><td>7</td></tr>
<tr><td>Rakeport</td><td>8</td><td>8</td><td>2</td><td>8</td></tr>
<tr><td>Founding Island - Spawn</td><td>9</td><td>9</td><td>7</td><td>9</td></tr>
<tr><td>Forgotten Isle</td><td>10</td><td>9</td><td>0</td><td>16</td></tr>
<tr><td>Founding Island - Bunker</td><td>11</td><td>10</td><td>8</td><td>10</td></tr>
<tr><td>Tavish Town</td><td>12</td><td>11</td><td>15</td><td>11</td></tr>
<tr><td>RTC - Global Control</td><td>13</td><td>12</td><td>4</td><td>12</td></tr>
<tr><td>RTC - Tower 3.0</td><td>14</td><td>13</td><td>11</td><td>13</td></tr>
<tr><td>East Village</td><td>15</td><td>14</td><td>5</td><td>14</td></tr>
<tr><td>Blakewood Outpost</td><td>16</td><td>15</td><td>10</td><td>17</td></tr>
<tr><td>Reborn X Museum</td><td>17</td><td>11</td><td>12</td><td>20</td></tr>
</tbody>
</table>
</div>

### Initialization

When a RCorp Rail subscriber enters the platform of a station (coordinates all manually defined in our `stationmsg` function) they will be prompted with the station selection screen. After picking a station, the system will then check if the user needs to specify a direction as most stations have two directions. If the user is at a station with only one direction, this will be skipped. The user will be given another screen to pick the direction, however one direction will be marked as recommended. This is done by subtracting the current station's coordinates from the destination station's coordinates and using the ideal grid system. This generally sends the user in the right way but may not be the fastest due to the limitations of the ideal model. For instance, a user at Spawn wanting to go to the Cruise Ship will be told to take RW-15 North to RW-12 West to the Cruise Ship. This does not take them in the absolute wrong way, however taking RW-15 South to RW-215 Dos Loop will actually be faster. The direction compared is only the one relevant to the station, so if the station runs North South then only North South position is checked. If there is no difference then the system will always recommend the positive variant (East/South)

After the user has selected a station and direction if needed, the system will then check if the invisible marker entities at pod spawning locations are available, and will only spawn the pod if they are. The user will then be marked as the `rcrailprimary` user, their pod will not depart until they have entered it. After they have entered, the doors will close and the pod departs. The user is given a screen in chat to change direction at any time if they want to go to a different station.

At each station set ID change, the function `applycoords` is ran, this assigns the x and z coordinate based on current rcsid. 

### Arrival

When the pod arrives at a station, the pod will stop and the doors will open. The station second slot behind it will then close up, allowing one more arriving pod to queue up while waiting for the first to depart/despawn. The user is then given a screen to change their destination if they want to go somewhere else. If they exit the pod the pod will begin a timer and destroy itself after a few seconds.

## Stations

The following is a full list and detail on RCorp Rail stations as of late 2026.

### Standard Station Model

{% include wiki-image.html file="/wiki/assets/images/rcrailstation/standardstation.webp" caption="The Standard Station Model, as seen from the Testing Sector. The departure/arrival module is visible below it" side="right" %}
The Standard Station Model was designed by Mr. Void and Mr. Ij during the summer of 2024 at the Founding Island - Spawn station. It consists of a three-block wide platform with two lanes on opposite directions on the sides, with the station bypass tracks adjacent to those. The departure modules are placed under the tracks and were designed specifically to fit within the Standard Model. All stations have been built following this model besides the two main stations at the Redstone Tower Complex and the Founding Island Bunker, which have their own unique designs. Note that some stations will remove up to 3 of the rail tracks depending on how the station is designed (one way, on a spur route, etc.)

### Admin Controls

Two RCorp Rail Stations are considered as "Main Stations". These were the first two stations of the original RCorp Rail plan in 2023 (FI Bunker station was built at this time, but RTC much later, however still following the original plan). These stations are the only two that have an Admin Control Room, which allow for the following for users with `rcorpsec ≥ 3` 

<div class="wiki-table-wrap">
<table>
<caption>Admin Room Controls</caption>
<thead><tr><th>Control</th><th>Function</th></tr></thead>
<tbody>
<tr><td>Ghost Pod Spawn delay</td><td>Adjusts the delay between ghost pod spawns. Options are 1 minute, 2 minutes, and 3 minutes.</td></tr>
<tr><td>Global Departure Shutoff</td><td>Shuts down all RCorp Rail departures. This is used for maintenance or emergencies.</td></tr>
<tr><td>Global Ghost Pod Shutoff</td><td>Shuts down all ghost pod spawns. This is used for maintenance or emergencies.</td></tr>
<tr><td>Ghost Pod Spawn max count</td><td>Adjusts the maximum number of ghost pods that can be spawned at once. Options are 5, 10, and 15.</td></tr>
<tr><td>Ghost Pod delay/threshold resets</td><td>Removes current tracking of delay and threshold. Note that the threshold button will also kill all loaded ghost pods</td></tr>
<tr><td>Block and divert from main station</td><td>Blocks and diverts all pods from the main station. This is different depending on which control room. FIBunker will diver to Main Bunker. RTC Tower 3.0 will divert to the Global Control station.</td></tr>
<tr><td>Cancel subscription</td><td>Allows a user to cancel their subscription in the maze. This is only available at the Tower 3.0 station.</td></tr>
</tbody>
</table>
</div>

### Testing Sector - Station 0

{% include wiki-image.html file="/wiki/assets/images/rcrailstation/testing.webp" caption="The Testing Sector RCorp Rail station, as seen from the ocean." side="left" %}
The testing sector runs north-south and is currently the western most station. Served by [RW-10](#rw-10) and [RW-11](#rw-11). It is one of three restricted stations that require RCorp clearance 2 or higher (Equivalent to a level 3 staff card). <br><br> The station uses the [Standard Station Model](#standard-station-model) and was one of the last stations of the initial bunch to be connected. The first pass and functionality was made by Ij, while Creepeton and Faiyaz worked on the outer design. This station does not have a purchasing module. The design is of a large closed sphere with openings for the rails and pedestrian bridge. On the other end is a wall with some credits for RCorp Rail. The station welcome sign marks it as being "Outer RW / Far Dos Region"

### Redstone Theme Park - Station 1

{% include wiki-image.html file="/wiki/assets/images/rcrailstation/themepark.webp" caption="The Redstone Theme Park Pirate Island with multiple highways entering, as seen from the north side of the ocean." side="right" %}
The Redstone Theme Park station runs north-south and was one of the most desired stations to have, and also one of the hardest to intregate. The Theme Park is quite far west, and required two U1 trips to reach from Founding Island. The theme park station is in the {% include wiki-link.html title="Pirate Island" %} area, in the same way as U1. [RW-13](#rw-13) and [RW-213](#rw-213) directly enter the Pirate Island, with the latter serving it. This has to be done due to the Pirate Island being very hard to fit RCorp Rail track into, nearly half a decade after its original construction. <br><br>The station uses the Standard Station Model, minus the two bypass tracks. The station was made by Ij, with minor tweaks by Sean and SomeYTguyFor1. It has a purchasing module in the U1 station at the themepark. The station welcome sign marks it as being "Central Dos"

### Redstone Cruise Ship - Station 2

{% include wiki-image.html file="/wiki/assets/images/rcrailstation/cruiseship.webp" caption="The Redstone Cruise Ship station, as seen from the ocean. The cruise ship itself is seen on the left side." side="left" %}
The Redstone Cruise Ship station runs north-south and was also heavily desired for the same reason. It was one of the earlier stations over a few iterations. The Cruise Ship was one of the most controversial stations in placement due to the {% include wiki-link.html title="RW Civil War" %}. The station was first made as a floating platform in the nearby lake, but was then moved to a grass platform more on the south side, putting it closer to the interchange with RW-113. This move made it easier to integrate the station, but put it very far from the original U1 station. We instead gave the station its own bridge to the cruise ship harbor. Served directly by [RW-13](#rw-13). <br><br>The station fully uses the Standard Station Model, including the bypass for RW-13. Both iterations of the station were made by Ij, with the cover by SomeYTguyFor1 and tweaks by Sean. It has a purchasing module along the cruise ship harbor. The station welcome sign marks it as being "Outer Dos"

### Dos Village - Station 3

{% include wiki-image.html file="/wiki/assets/images/rcrailstation/dosvillage.webp" caption="The Dos Village station, as seen from the outside." side="right" %}
The Dos Village station was the first one-way station. It sends the rider west to follow the Dos Loop counterclockwise. It was a difficulty to integrate due to the Dos Village station already having a plethora of U1 tracks, but space was found next to the Main Bunker departure module. Served directly by [RW-215](#rw-215--rw-215-ccw). <br><br>The station uses the Standard Station Model at its most minimum state, with only a single track and no bypass that circles back onto the route. The station was made by Ij, with the cover by SomeYTguyFor1 and then redone by EzraThunder. It has a purchasing module inside the Dos Village U1 station. The station welcome sign marks it as being "Central Dos"

### Main Bunker - Station 4

{% include wiki-image.html file="/wiki/assets/images/rcrailstation/mainbunker.webp" caption="The Main Bunker station, as seen from the outside." side="left" %}
The Main Bunker station was one of the first stations planned, and has a very strange setup. Originally, the Bunker was split into a Bunker South and Bunker North Mountains stations to coincide with the RCorp expansion of the Main Bunker (which has not happened at time of writing), with the south being part of Dos Loop and the north a different highway. However, the stations were moved to be right next to each other and seemingly together, however that split is still there. It operates as one station running north-south, but in reality it has South marked as being "Dos Loop" and north as being "Outer Dos", for the north the departing rider could head either direction. Served by [RW-315](#rw-315) for Dos Loop and [RW-512](#rw-512) for Outer Dos. <br><br>The station uses the Standard Station Model, with no bypasses. The station was made by Ij, with the cover by SomeYTguyFor1. It has a completely covered bridge and walkway to the purchasing module inside the Main Bunker entrance. The station welcome sign marks it as being "Central Dos"

### SMP Base - Station 5

{% include wiki-image.html file="/wiki/assets/images/rcrailstation/smpbase.webp" caption="The SMP Base station, as seen from the outside." side="right" %}
It was desired for a station in the Dos Prairie, however it was unsure to us whether we would put it at the SMP Base station or the actual Dos Prairie station. We decided to use the SMP Base since it was right against the loop. The station is one-way, sending the rider north along the Dos Loop. Served by [RW-215](#rw-215--rw-215-ccw). <br><br>The station uses the Standard Station Model at its own most minimum state. The station was made by Ij, with the cover by SomeYTguyFor1. The purchasing module is inside the SMP Base. The station welcome sign marks it as being "Central Dos"

### Gerudo Desert - Station 6

{% include wiki-image.html file="/wiki/assets/images/rcrailstation/gerudo.webp" caption="The Gerudo Desert Station, as seen from the platform side." side="left" %}
The Gerudo Desert station was made to honor the original U1 gerudo station from a very long time ago. It runs east-west. Served by [RW-215](#rw-215--rw-215-ccw) with the westbound returning to the Dos Loop while the eastbound ends the 215 loop at the FI Bunker. <br><br> The station uses the Standard Station Model, minus one bypass. The station was made by Ij originally, but fully transformed by EzraThunder to a desert theme with a clocktower. The entrance to the platform was moved underground with stairs and an elevator to access it from the purchasing station. It also has a small garden inside of it. The station welcome sign marks it as being "FI West Outpost / Outer Dos"

### Redstone Villa - Station 7

{% include wiki-image.html file="/wiki/assets/images/rcrailstation/villa.webp" caption="The Redstone Villa Station, as seen from the ocean side." side="right" %}
The Redstone Villa station was made to give the Villa more presence in the world than just a random U1 tunnel in the Gerudo Desert. It runs north-south. Served by [RW-120](#rw-120). <br><br>The station fully follows the Standard Station Model. The station was made by Ij originally, but had another similar full transformation by EzraThunder in an overgrown style. It has an elevated platform accessible from below by stairs or elevator. The station welcome sign marks it as being "Outer Dos"

### Blakewood Travel / Rakeport - Station 8
{% include wiki-image.html file="/wiki/assets/images/rcrailstation/rakeport.webp" caption="The Rakeport Station, as seen from the platform side." side="left" %}
The Rakeport station also known as Blakewood Travel was one of the key original planned stations, designed to help RCorp in the Rakegame. There were many scrapped plans for it, mainly due to challenges from the elevated RW-12 above. The final plan was then to put the station below, and have a spur to access it. The station is technically one way with the highway both terminating and starting at the station, however the quick interchange with RW-12 makes it an east-west station. Served by [RW-312](#rw-312). <br><br>The station follows the Standard without bypasses, and the arrival acts as a simple instant kill for pods. The station was made by Ij, Void, and LLucas originally, but fully transformed by EzraThunder to be a unique styled complex that contains a newsboard, the RCRail Map, and some other images. The purchasing station is right against the Blakewood Travel entrance and original U1 station. The station welcome sign marks it as being "Blakewood Travel / Outer FI"

### Founding Island Spawn - Station 9

