---
title: "RCorp Rail"
order: 9
section: "Transport Infrastructure"
description: "RCorp Rail is Redstoneworld's latest transport network. It connects all major landmarks and sectors in Chapter 7 using distinct highways and pods."
image: "/wiki/assets/images/rcrailbanner.webp"
image_alt: "RCorp Rail track and pods at the Global Control RTC Station."
last_modified: "2026-09-18T04:02:30Z"
contributor: "LLucas"
infobox: {"Started": "July 5th, 2023", "Project Directors": "Mr. Ij, Mr. Void, LLucas, EzraThunder, SomeYTguyFor1", "Completed":"March 18th, 2026", "Type": "Global Infrastructure"}
published: true
---

RCorp Rail is the latest transportation system on Redstoneworld. Designed to be both a companion and successor to the old {% include wiki-link.html title="U1" %} system, RCorp Rail uses two player pods, a fast speed, interconnected rails, and a subscription model to move users around efficiently and economically. 

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
RW-11 is the other end of the Testing Sector station. It heads south before turning east and terminating at an interchange with RW-13/RW-20 at the {% include wiki-link.html title="Redstone Theme Park" %}.
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
RW-317 is a spur from that runs northwest to serve the Reborn X Museum and uses RW-15 to terminate.
#### RW-20
RW-20 is the far southern east-west route. It starts east of the interchange with RW-11 and RW-13 at the Waterpark. It heads east, wrapping around the south Dos Mountains where it has an interchange with RW-120. It continues to its Tavish Town Station and then the interchange with RW-17. Afterwards there is a brief north stretch to the interchange with RW-112 where it then shoots east for the Blakewood Forest while wrapping around the barrier. It terminates just north of the Blakewood Forest station.
#### RW-120
RW-120 is a spur that runs northwest from RW-20 to serve the Villa station, then terminating at the Dos Loop RW-215.
#### RW-220
RW-220 is the Blakewood Forest emergency bypass. It quickly takes an unauthorized rider out of the zone to then end back at RW-20.

## Pod speed mechanics

The RCorp rail pod uses a myriad of entities, including block displays, a pig and famously, a tadpole mounted on a minecart. Below the main highway there is an ordinary minecart track, and therefore the default speed of the RCorp rail pod is 0.4 blocks/tick (8 blocks/sec at 20 TPS). However, on straight sections, the RCorp pod has the ability to accelerate to a much higher speed, allowing it to traverse the world faster than a U1 cart.

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
