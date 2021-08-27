
  
# Make Component For NextJS & Styled-Components  
  
This project was created to make a simple CLI that can automagically create the necessary files and folders as well export a new component for NextJS usuing styled components.  
  
This was made entirely in Python with no dependencies.  
  
## Installation  
  
To install just run the `install.sh` file.  
Or run the following `pip installl -e /path/to/directory`

## Usage

To use Make Component, simply type `mkcomponent` and pass two parameters. The first parameter is the name of the component. The second is the name of the Styled Component. The Styled Component and Component cannot be the same name as it will cause issues in your JS file.


### Example
`mkcomponent slider wrapper`

Here we are making a slider component and we will call the parent Styled Component wrapper.

## Issues & Fixes

If the `mkcomponent` command is not working, you may need to type `python -m mkcomponent`
However, if you would like to make it work without the prefix, you can edit your `.bashrc` file and create a alias.

### Example
Edit the file with `nano ~/.bashrc`

At the bottom of the file add `alias mkcomponent='python -m mkcomponent'`

This will allow the component to work with just `mkcomponent` everytime.