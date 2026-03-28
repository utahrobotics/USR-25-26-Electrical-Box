# Future-proofing Electrical Plans SP2025
This document is intended to serve as essentially a "wishlist" of sorts regarding future organization and development of the Electrical subsystem.

## Generic GPIO blocks
-   Group blocks of generic digital/analog GPIO pins on backplane layout. These can then be allocated as needed as things progress so that at the very least, there is a known pinout to work off of.
-   This also brings the advantage of the backplane pinout becoming decoupled from specific use-cases, meaning that a single change involving the pinout of one board **will not** result in changes rippling across every other board.
    - Take advantage of KiCAD's "rule zones" features to set netclasses on otherwise generic pins

## Defined PCB size classes
-   Provide blank PCB templates using KiCAD's recently-added "design blocks" feature that allows for schematic and PCB components to be exported in blocks and be available for use between any projects that import the block library.
-   Basic "small", "medium", and "large" blocks exist as square sizes
-   Variant "small-wide", "medium-wide", and "large-wide" also exist
-   Narrow variants might not necessarily exist depending on edge connector choice
    -   To address this, multiple different edge connector types may also be made available for use within the libraries for greater flexibility

## Reusable design blocks
-   Building off of the design blocks that will be utilized for PCB templates, complete component design blocks (matched schematic and PCB layout blocks in pairs) may also be added with unique identifiers that provide an at-a-glance description of functionality (for example, voltage conversion)
-   This alongside custom schematic symbols footprints may be very useful
-   If it comes to it, the logical extension of this would be for the design blocks to literally exist as mini-PCBs that can be independently added to a design either explicitly (plugs into headers/is soldered onto the rest of the board like a sort of PCB "patch") or implicitly (integrated into the rest of the design without the need for soldering)
-   As decisions are made down the line in other subteams, design blocks can then be quickly swapped in and out
    -   If possible, lining up the input and output lines on both the schematic block and PCB layout block would make such swapping of components effectively seamless regarding routing. Likely would be overkill to do this though, and simply having it be labeled as a specific design block region may be enough.
-   This follows the trend that has occurred across the team with increasingly modular designs as well, and overall should hopefully result in much greater flexibility that reduces the team's reliance on decisions being made by other teams.

## Make criticial decisions first and foremost and *stick with it*
-   The assumption of the electrical subsystem existing in a vacuum and thus capable of designating for itself as much space as desired is only made in the earliest stages of prototyping when designs and functionality are being tested.
-   Design for as compact of a PCB layout as possible. Routing-wise, this may mean it becomes necessary to rely on sub-PCBs to make a pseudo-4 layer board in a "PCB sandwich" style build.
-   "Large" and "Large wide" boards especially are discouraged from being used as part of the final design
-   Designing for the minimal space use makes electrical box placement much more flexible, but the minimum size *must* be enforced on other sub-teams in their designs. If we say that we cannot go below a certain size, drill it into the other teams such as Mechanical so that they know that that is a **hard limit** that cannot be passed. 
    -   No space for an already minimum-size electrical box? No robot.
    -   TL;DR: Electrical sub-team cannot continue to exist in a "reactionary" state where it designs based exclusively on the decisions of other sub-teams.

## Designate "Design Mentor" role(s) within the subteam
-   These roles exist to guide and approve of designs prior to protototyping and production. Ideally, they should have some degree of expertise in the field they mentor in.
    -   For example: A hypothetical **Layout Mentor** role has longtime experience in schematic and PCB layout. They should work with team leads (or perhaps they *are* one of the leads) to produce a **design guidelines** document. This establishes what should be taken into consideration in a given design, and suggested values for aspects such as trace width.
-   Closer to the competition when designs for the final PCBs are being laid out, these mentors will work directly with those doing the designing to ensure that the PCB designs will, in simple terms, "work". They should look for obvious mistakes that may compromise a robot's ability to function or cause harm to other parts of the design, and assist in the redesigning process if need be.