---
title: "RTC Reactor"
order: 8
image: "/wiki/assets/images/rtcrisland_bliss.webp"
section: "RTC Power Infrastructure"
image-alt: "The RTC reactor island, as viewed from the balcony on the mall floor of RTC-2"
description: "The RTC-Blakewood Nuclear Power Plant, located on Floor -1 of Tower 3.0 in the RTC."
infobox: {"Started":"January 9th, 2025","Reactor Technical Start":"August 26th, 2025","Head builders and designers":"LLucas, Mr. Ij, SomeYTGuy, EzraThunder","Technical work":"LLucas, Mr. Ij","Approximate total number of commands":"1400","Sector":"Redstone Tower Complex (RTC)"}
last_modified: "2026-09-15T03:11:00Z"
contributor: "LLucas"
---

The RTC reactor is the newest reactor on Redstoneworld. Situated on the bottom of Tower 3.0 (in the industry complex), it is the most complicated and therefore realistic reactor on the map.

## Design and Use in the World

{% include wiki-image.html file="/wiki/assets/images/rtcr-powertofi.webp" caption="Powerlines from the Tower 3.0 to the FIB" side="left" %}
The RTC reactor was designed to power a huge amount of the map's infrastructure. Notably, the RTC complex and the Blakewood region. It also serves as a backup to many parts of the map, in case other power systems fail. For example, it is able to fix the FI bunker reactor, provide power to the Dos region (in case of a power failure). Furthermore, it can also provide huge bursts of energy to the RTC-2 probes, which are designed to fight the anti-catalyst probe on RTC-1. Since the amount of power required for a probe burst can exceed the amount of energy that the reactor can produce, the aux battery gets used.

{% include wiki-image.html file="/wiki/assets/images/rtcr-ubs.webp" caption="The reactor's UBS (Upper Biological Shield)" side="full" %}
The RTC reactor is designed based off two real world reactor designs. Most of the rooms, turbine halls, etc. are based off of the RBMK reactor model. However, most of the functionality and technical aspects are based off a PHWR (Pressurized Heavy Water Reactor).

## Radiation System

The RTC reactor is the first system that implements radiation application every tick, rather than it being applied all at once every ingame "hour" (usually around one real life minute). Furthermore, it also implements small amounts of radiation doses which can be tracked using a dosimeter.
{% include wiki-image.html file="/wiki/assets/images/rtcr-radcmds.webp" caption="The reactor radiation command system, as viewed with fullbright. Built on Jan 12, 2025 by LLucas. Contains over 180 commands." side="full" %}

The entire radiation system was placed in a one chunk area, which allowed it to be easily loaded and unloaded (which can be trivially achieved) and was built before the datapack GitHub infrastructure was implemented.

### Bossbar

The bossbar displays the current radiation dose rate, formatted with proper units in sieverts per hour. Based off the radiation level, the fullness of the bossbar, the formatting and precision can change.

<div class="wiki-table-wrap">
<table>
<caption>Bossbar formatting, colour and fullness at different radiation levels</caption>
<thead><tr><th>Radiation level</th><th>Radiation value format</th><th>Bossbar & text colour</th><th>Bossbar fullness</th></tr></thead>
<tbody>
<tr><td>Less than 250 nSv/h</td><td>##.00 µSv/h</td><td>Green bar, Green text (#00FF00)</td><td>0/10 notches</td></tr>
<tr><td>0.25 µSv/h to 4.99 µSv/h</td><td>##.00 µSv/h</td><td>Green bar, Green text (#00FF00)</td><td>1/10 notches</td></tr>
<tr><td>5.00 µSv/h to 49.99 µSv/h</td><td>##.00 µSv/h</td><td>Green bar, Green text (#00FF00)</td><td>2/10 notches</td></tr>
<tr><td>50.00 µSv/h to 99.99 µSv/h</td><td>##.00 µSv/h</td><td>Green bar, Green text (#00FF00)</td><td>3/10 notches</td></tr>
<tr><td>100 µSv/h to 499 µSv/h</td><td>### µSv/h</td><td>Green bar, Green text (#00FF00)</td><td>3/10 notches</td></tr>
<tr><td>500 µSv/h to 999 µSv/h</td><td>### µSv/h</td><td>Yellow bar, Yellow text (#FFFF00)</td><td>4/10 notches</td></tr>
<tr><td>1.000 mSv/h to 3.999 mSv/h</td><td>#.000 mSv/h</td><td>Yellow bar, Yellow text (#FFFF00)</td><td>4/10 notches</td></tr>
<tr><td>4.000 mSv/h to 9.999 mSv/h</td><td>#.000 mSv/h</td><td>Yellow bar, Yellow text (#FFFF00)</td><td>5/10 notches</td></tr>
<tr><td>10.00 mSv/h to 14.99 mSv/h</td><td>##.00 mSv/h</td><td>Yellow bar, Yellow text (#FFFF00)</td><td>5/10 notches</td></tr>
<tr><td>15.00 mSv/h to 49.99 mSv/h</td><td>##.00 mSv/h</td><td>Yellow bar, Yellow text (#FFFF00)</td><td>6/10 notches</td></tr>
<tr><td>50.00 mSv/h to 99.99 mSv/h</td><td>##.00 mSv/h</td><td>Red bar, Orange text (#FF4500)</td><td>7/10 notches</td></tr>
<tr><td>100 mSv/h to 149 mSv/h</td><td>### mSv/h</td><td>Red bar, Red text (#FF0000)</td><td>7/10 notches</td></tr>
<tr><td>150 mSv/h to 499 mSv/h</td><td>### mSv/h</td><td>Red bar, Red text (#FF0000)</td><td>8/10 notches</td></tr>
<tr><td>500 mSv/h to 999 mSv/h</td><td>### mSv/h</td><td>Red bar, Red text (#FF0000)</td><td>9/10 notches</td></tr>
<tr><td>1000 mSv/h to 9999 mSv/h</td><td>(obfuscated) Sv/h</td><td>Purple bar, Purple text (#AA00AA)</td><td>10/10 notches</td></tr>
<tr><td>In excess of 10 Sv/h</td><td>Whole bar obfuscated</td><td>Purple bar, Purple text (#AA00AA)</td><td>10/10 notches</td></tr>
</tbody>
</table>
</div>
