# Mapping and Mosaic Mission
  
## About
  This mission is about that _ROV_ flying a transect line over the search area. 
  
  The search area of the wreck will be simulated by a ½-inch PVC pipe rectangle 3 meters long by 1 meter wide.A **grid** of 8 rectangles, 75 cm x 50 cm.
  
  ![Map](https://raw.githubusercontent.com/AntonAshraf/Materials/main/MATE%202022/MAP.png)
 #### There are many subtasks in the mission:
  - Start from any side from black pipe
  - keep the camera of the ROV see the 2 blue pipes
  - Avoid to see the Red pipes
  - Take 8 photos for 8 rectangles of the grid
  - Display the 8 photos
  - stitch the images into photomosaic
  - Display Map with wreck of the ship
  
## Approach
  
  We take every thing to do in one shot. starting from the begining we will take only 4 photos 
  while crossing the map and then trying to crop it to take the ROI _"Region of intrest"_ and the pass it 
  to a function that split it into 2 halves and safe it all in a directory.
  
  ##### Make some outputs
  From the directory we read the images 2 times
  1. Display the 8 images randomly in one Window
  2. stitch the images into photomosaic

  Last thing is to read image of the map and draw 3 lines indacates to the location of the _Ship Wreck_
  
  ## TO DO:
  - [x] Push all codes separately
  - [x] Check every file is working
  - [x] Make main.py file
  - [x] main.py is ready to run
  - [x] Display the Mosaic in correct order
  - [x] Fill the Requirments file
  - [x] Fix _holding_ on S button
  
  - [ ] Display the 8 images in **one** window
  - [ ] Make screen size Larger (without rescaling)

  
  
