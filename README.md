<p align="center">
  <picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/user-attachments/assets/6595b585-a8dc-4f09-8024-5df15d498cac" width="150px">
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/user-attachments/assets/6595b585-a8dc-4f09-8024-5df15d498cac" width="150px">
  <img alt="Substance 3D Designer Logo" src="https://github.com/user-attachments/assets/6595b585-a8dc-4f09-8024-5df15d498cac" width="50px">
</picture>

 
</p>

<h1 align="center">Random Frame Colors</h1>


Random Frame Colors is a Substance 3D Designer plugin that offers an alternative to a built-in "Add frame" functionality. When used, newly created frames are automatically assigned a random, visually distinct color instead of the default blue.


<p align="center">
  <picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/user-attachments/assets/6f07f3f9-f31b-49cf-9e25-2fec4d0c39a6" width="1000px">
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/user-attachments/assets/6f07f3f9-f31b-49cf-9e25-2fec4d0c39a6" width="1000px">
  <img alt="Creating frames - gif" src="https://github.com/user-attachments/assets/6f07f3f9-f31b-49cf-9e25-2fec4d0c39a6" width="400px">
</picture>

 
</p>

---
# 15 Visually distinct colors! 🎨

When creating a frame, the plugin chooses one of the 15 visually distinct colors available by default. During one session, it will not choose the same color anymore, until all of the options are used.

Also, the options are ***easily customizable!***

<p align="center">
  <picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/user-attachments/assets/30059cd5-beeb-4747-99bb-daab4dff0a1b" width="1566px">
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/user-attachments/assets/30059cd5-beeb-4747-99bb-daab4dff0a1b" width="1566px">
  <img alt="Colors Showcase" src="https://github.com/user-attachments/assets/30059cd5-beeb-4747-99bb-daab4dff0a1b" width="1566px">
</picture>

 
</p>

---

# How to install the plugin:

1. Download the latest plugin (random_frame-colors.zip) here:
   https://github.com/vovkmariia/random-frame-colors/releases/latest

2. Look up the default directory for your Substance Designer plugins

3. From the extracted folder copy "random_frame_colors" and paste it into the default directory

4. Restart the application

5. Once Designer is restarted, the plugin should be loaded. But just in case, open Tools -> Plugin Manager again and check that the checkbox of the plugin is enabled

<p align="center">
  <picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/user-attachments/assets/16470667-7a6f-4558-b14d-723e19485c47" width="1022px">
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/user-attachments/assets/16470667-7a6f-4558-b14d-723e19485c47" width="1022px">
  <img alt="Installation Guide" src="https://github.com/user-attachments/assets/16470667-7a6f-4558-b14d-723e19485c47" width="1022px">
</picture>

 
</p>

---
# How to use it

After installing the plugin and opening a graph, you should be able to see a new button in your top toolbar that looks like this:

<p align="center">
  <picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/user-attachments/assets/704818eb-62b6-417b-ac5c-83bc491e4bb7" width="100px">
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/user-attachments/assets/704818eb-62b6-417b-ac5c-83bc491e4bb7" width="100px">
  <img alt="Creating frames with editor open - gif" src="https://github.com/user-attachments/assets/704818eb-62b6-417b-ac5c-83bc491e4bb7" width="100px">
</picture>

 
</p>

Select the nodes you want to group and click this button. 

You can undo the creation of a frame with `Ctrl + Z`. If you click the button again after that, it will generate a new color!

---
# How to add your own colors!

1. Navigate inside the plugin folder and open up `colors.py` in any text editor of your choice

2. Add / remove / modify custom colors by entering a name and an RGB value in 0-1 format (Rapidtables has a great tool for converting HEX color codes into 0-1 values - https://www.rapidtables.com/convert/color/hex-to-rgb.html)

<p align="center">
  <picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/user-attachments/assets/69272835-f6bd-4db2-895f-14171a446972" width="2042px">
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/user-attachments/assets/69272835-f6bd-4db2-895f-14171a446972" width="2042px">
  <img alt="Custom Colors" src="https://github.com/user-attachments/assets/69272835-f6bd-4db2-895f-14171a446972" width="2042px">
</picture>

 
</p>

---
# How it works 👾

The idea for this simple plugin was inspired by a very minor inconvenience I encountered while working with Substance Designer - it felt like the default behavior of assigning a static default color to each newly created frame was not the best choice. I didn't like manually going over to the color picker and trying to click on a color that is not the default blue, not too garish, and not too similar to the frames I already have. So I decided to write a randomizer of hand-picked visually distinct colors.

There are other similar plugins that are meant to help with the colors of the frames in Substance Designer (and I am grateful to the creators for the inspiration!).

<p align="center">
  <picture>
  <a href="https://etereaestudios.com/2022/12/13/frame-colors-plugin-for-designer/"> <source media="(prefers-color-scheme: dark)" srcset="https://github.com/user-attachments/assets/026af3b1-b26c-43cd-ab37-6b42b7e96dd8" width="1866px"> </a>
  <a href="https://etereaestudios.com/2022/12/13/frame-colors-plugin-for-designer/"> <source media="(prefers-color-scheme: light)" srcset="https://github.com/user-attachments/assets/026af3b1-b26c-43cd-ab37-6b42b7e96dd8" width="1866px"> </a>
  <a href="https://etereaestudios.com/2022/12/13/frame-colors-plugin-for-designer/"> <img alt="Eterea Frame Colors" src="https://github.com/user-attachments/assets/026af3b1-b26c-43cd-ab37-6b42b7e96dd8" width="1866pxx"> </a>
</picture>

 
</p>

<p align="center">
  <picture>
  <a href="https://marcovitale.gumroad.com/l/mvcolorframes"> <source media="(prefers-color-scheme: dark)" srcset="https://github.com/user-attachments/assets/adfab6e8-1290-47eb-abd1-a6ef79a56f10" width="1879px"> </a>
  <a href="https://marcovitale.gumroad.com/l/mvcolorframes"> <source media="(prefers-color-scheme: light)" srcset="https://github.com/user-attachments/assets/adfab6e8-1290-47eb-abd1-a6ef79a56f10" width="1879px"> </a>
  <a href="https://marcovitale.gumroad.com/l/mvcolorframes"> <img alt="MV Color Frames" src="https://github.com/user-attachments/assets/adfab6e8-1290-47eb-abd1-a6ef79a56f10" width="1879pxx"> </a>
</picture>

 
</p>

But they both share one common trait - colorization applies only to already existing frames in the graph. I wanted to randomize the color of the frame immediately after creating it, without any manual color assignment.
  
Therefore, I had to replicate the native “Add Frame” functionality in Python from scratch, while adding some randomization of color in between.

The main function of the plugin is stored in the Toolbar class, which allows adding a custom button to the Substance Designer's Ui and not running the script through the Python Editor.

<p align="center">
  <picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/user-attachments/assets/08204a97-5991-42f7-a170-be7b7b981f8e" width="1668px">
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/user-attachments/assets/08204a97-5991-42f7-a170-be7b7b981f8e" width="1668p">
  <img alt="Toolbar Class" src="https://github.com/user-attachments/assets/08204a97-5991-42f7-a170-be7b7b981f8e" width="1668px">
</picture>

 
</p>

After getting the current active graph in the application window, the program retrieves all of the selected nodes in the graph and calculates the bounding box for the frame based on the nodes' positions.

<p align="center">
  <picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/user-attachments/assets/122a0e08-3242-4238-b144-e80366327935" width="1672px">
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/user-attachments/assets/122a0e08-3242-4238-b144-e80366327935" width="1672p">
  <img alt="Calculating the bounding box" src="https://github.com/user-attachments/assets/122a0e08-3242-4238-b144-e80366327935" width="1672px">
</picture>

 
</p>

When the plugin initializes, it creates a temporary copy of all of the color options from the separate `colors.py` file. Using `random.choice()` , the program selects one of the options each time the function is called. After that, it deletes the corresponding entry from the dictionary of available colors. This ensures that while there are still unused colors, it will not generate a duplicate. Temporary dictionary resets every time it becomes empty.

<p align="center">
  <picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/user-attachments/assets/8f19ca3c-375d-4536-aad4-8f0ae14e2fe6" width="1679px">
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/user-attachments/assets/8f19ca3c-375d-4536-aad4-8f0ae14e2fe6" width="1679px">
  <img alt="Calculating the bounding box" src="https://github.com/user-attachments/assets/8f19ca3c-375d-4536-aad4-8f0ae14e2fe6" width="1679px">
</picture>

 
</p>

And just like that, we create a frame with a unique color every time 🙂

<p align="center">
  <picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/user-attachments/assets/f756bf14-fec0-4015-93b6-de64c9b2e9f7" width="1500px">
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/user-attachments/assets/f756bf14-fec0-4015-93b6-de64c9b2e9f7" width="1500px">
  <img alt="Creating frames with editor open - gif" src="https://github.com/user-attachments/assets/f756bf14-fec0-4015-93b6-de64c9b2e9f7" width="400px">
</picture>

 
</p>

---

# Help!

If you encounter any issues with the plugin, please reach out to me via email:
mariia.vovk.contact@gmail.com

I will try my best to help!
