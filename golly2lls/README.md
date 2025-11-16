# Golly to LLS

## Uses a 32-state rule to generate LLS patterns.

"X" cells (states 16 and above) correspond to apostrophes.
Darker versions of subperiodic/variable/asterisk cells do not affect cells differently.

Here's basically a step-by-step process of how I use these scripts:

1. Generate a pattern.	
	1. Find partials on LifeWiki (or ConwayLife Forums, etc.), and use set_subperiod.py to cut off the partial at certain areas for extension.
	2. Manually make an area of subperiodic cells.
2. Run in LLS.
	1. If it is proven unsatisfiable in preprocessing, I usually just rebuild the pattern or try something else.
	2. If it is proven unsatisfiable after a few seconds, I try to expand the area to something larger.
	3. If I get a good result but it still has apostrophe cells, I cut the partial again and repeat.

I've never completed a partial with this, but hopefully it'd be helpful to some.