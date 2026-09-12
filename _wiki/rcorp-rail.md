---
title: "RCorp Rail"
order: 9
section: "Transport Infrastructure"
description: "RCorp Rail is Redstoneworld's latest transport network. It connects all major landmarks and sectors in Chapter 7 using distinct highways and pods."
image: "/wiki/assets/images/rcrailbanner.webp"
image_alt: "RCorp Rail track and pods at the Global Control RTC Station."
last_modified: "2026-9-12T01:20:25Z"
contributor: "Ijdtm7"
infobox: {"Started": "July 5th, 2023", "Project Directors": "Mr. Ij, Mr. Void, LLucas, EzraThunder, SomeYTguyFor1", "Completed":"March 18th, 2026", "Type": "Global Infrastructure"}
published: true
---

RCorp Rail is the latest transportation system on Redstoneworld. Designed to be both a companion and successor to the old {% include wiki-link.html title="U1" %} system, RCorp Rail uses two player pods, a fast speed, interconnected rails, and a subscription model to move users around efficiently and economically. 

It was first proposed in 2023 during {% include wiki-link.html title="Chapter 6" %} by Mr. Void.

Note that a video deep dive of RCorp Rail is available as <a href="/wiki/ijs-devlogs/#devlog34">Devlog 34</a>, it goes into detail on all stations as well as the code.

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
#### RW-17
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