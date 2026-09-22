---
title: "RTC Reactor"
order: 8
image: "/wiki/assets/images/rtcrisland_bliss.webp"
section: "RTC Power Infrastructure"
image-alt: "The RTC reactor island, as viewed from the balcony on the mall floor of RTC-2"
description: "The RTC-Blakewood Nuclear Power Plant, located on Floor -1 of Tower 3.0 in the RTC."
infobox: {"Started":"January 9th, 2025","Reactor Technical Start":"August 26th, 2025","Head builders and designers":"LLucas, Mr. Ij, SomeYTGuy, EzraThunder","Technical work":"LLucas, Mr. Ij","Approximate total number of commands":"1400","Sector":"Redstone Tower Complex (RTC)"}
last_modified: "2026-09-22T14:32:19Z"
contributor: "LLucas"
math: true
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

### Radiation calculation

The radiation value is calculated based off of a large amount of factors. Including radiation from the reactor itself, emergencies, and radiation decay.

#### Units

When building the radiation system, one of the goals was to be able to display a background radiation value (0.08 microsieverts/hour). Hence, the radiation value had to be compatible with a newly named dose rate unit known as "fracs" which was equivalent to 0.01 microsieverts/hour (or 10 nSv/h). Every tick, the reactor radiation value would be added to each player's radiation "frac" value (which is displayed to some extent on the dosimeters). Since one hour was considered as 1000 game ticks, adding a dose rate frac to the dose value frac would give the radiation dose frac unit a value of 10 pSv (or 0.01 nanosieverts).

For every 100 million dose rate fracs that accumulate, a millisievert is added to the player's `radiationdose` value.

#### System 1 & 2

Due to the use of fracs, there is potential for integer overflow in the decay equation (as seen below) at radiation values of approximately 2.14 Sv/h. Hence, at radiation values exceeding 1 Sv/h, the radiation system will switch from System 1 to System 2 (which uses millisieverts instead of fracs), appropriately converting the System 1 radiation value to millisieverts/hour. Conversely, when the radiation value drops below 1 Sv/h while System 2 is enabled, the System 2 millisievert value is converted back to fracs and System 1 is re-enabled. System 2 has the potential to overflow at approximately 214748 Sv/h, and is therefore capped at 100000 Sv/h (the real radiation values get nowhere near this, though) which is enough to kill a player 50 times over in a single tick.

#### Decay

The radiation decay system triggers every 180 game ticks (approx. 9 seconds) when the radiation value is above 0.08 microsieverts/hour. Each time a decay triggers, the radiation is divided by 1.1 (however this division does not affect the 80 nSv/h background radiation) via a multiplication by 10 and a division by 11. With these parameters, it can be determined that the half-life of this radiation is approximately 1309 ticks (~65.45 seconds). Note that the division is an integer division. For System 2, background radiation is considered negligible.

System 1:
\\[
\dot{H}\_{new} = \frac{10(\dot{H}_{old}-8)}{11} + 8
\\]

System 2:
\\[
\dot{H}\_{new} = \frac{10\dot{H}_{old}}{11}
\\]

_Note that radiation dose rate is denoted by \\(\dot{H}\\)_

#### Radiation from Reactor Operation

The radiation equation is relatively complex, as it involves numerous factors such as RCB (Reactor Containment Building) integrity, core temperature, water pressure, the current water type, and the fuel used. Due to the nature of this equation, which executes every tick, each frac added in this equation is equivalent to a radiation value that approaches appxoimately 1800 to 1980 fracs (depending on decay, 1800-1980 fracs is 18-19.8 microsieverts/hour).

##### Core temperature, RCB breach

Rather than using the raw core temperature, the radiation equation uses the core temperature target (the value the core temp is set to approach, \\(T_{target}\\)). For every degree above 175 Celsius, 10 fracs are added (this value can be negative). If the RCB is fully breached, however, this becomes 120 fracs per degree (corresponding to a \\(W_{RCB}\\) of 12).

##### Water pressure

Similarily to core temperature, the target water pressure \\(p_{target}\\) value is also used. For every 40 kPa increase in the water pressure target, one frac per tick is removed.

##### Turbine power, water type, fuel type

As with the other variables, turbine power \\(P_{target}\\) target is used over the raw value as well. For every 7 MW of turbine power, one frac is added. However, this value is multiplied by 2 when using light (non-distilled) water (corresponding to a \\(W_{water}\\) of 2), and is also multiplied by 2 (this can stack) when using enriched fuel rods (corresponding to a \\(W_{fuel}\\) of 2).

##### Equation

\\[
\Delta\dot{H}\_{tick} = \max(10(W_{RCB})(T_{target}-175) - \frac{1}{40}p_{target} + \frac{1}{7} W_{water} W_{fuel} P_{target}, 0)
\\]

_Note that the actual dose rate value approaches approximately 1800-1980 times the \\(\Delta\dot{H}\_{tick}\\) value, and that the default weighing factors (\\(W\\) values) are 1._

#### Emergency-related radiation

Emergencies can cause enormous spikes in radiation, which allows it to reach levels that can kill players in a couple seconds.

If core temperature is kept too high, the fuel rods can begin melting. When they start melting, a warning message is sent along with a 100 mSv/h radiation spike. Once the fuel rods fully melt, a 5 Sv/h spike is administered. However, if the fuel rods fully melt while the RCB is breached, a 15 Sv/h radiation spike is administered instead. During the fuel rod repair kit activation, radioactive material is purged into the atmosphere and 1600 mSv/h are added to the reactor complex.

Similarily, if the RCB begins being damaged, a warning message appears with chat, however, no radiation is administered. Once the RCB fully breaches, 2.5 Sv/h are added to the reactor complex (unless the fuel rods have already fully melted, in which case this becomes a 12.5 Sv/h radiation spike instead).

During a limbo level explosion (either caused by the AI or the player), a 1000 Sv/h radiation spike can be observed.

#### Radiation spewing mechanism

#### Dose rate advancements


