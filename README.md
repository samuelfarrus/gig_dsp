# GIG - DSP

Genshin Impact Generator for Data Science Projects

Coded by [samuelfarrus](https://github.com/samuelfarrus).

Las updated: **16/11/2021**, *Moment of Bloom* banner (rerun).

## Description

GIG - DSP is a .py file that offers a interactive random wish list generator through a terminal CLI simulation. It generates a .csv file containing as much wishes as desired, intented in the development of Data Science projects, data analysis projects, or whatever other reason.

GIG - DSP also considers a simulation of Genshin's (in)famous Pity System. It means that:

1. The generator will provide a guaranteed 4 stars item every 10 wishes.
	* If the guaranteed item is not a rate-up 4 stars character, the next guarantee will be necessarily a rate-up character.
2. Also, the generator will provide a guaranteed 5 stars character every 90 wishes.
	* If the guaranteed character in this case is not the rate-up 5 stars character, the next guarantee will be necessarily the rate-up one.

## Running GIG - DSP

To run GIG - DSP, simply open the terminal (or Git Bash) and type `py gig_dsp.py`, replacing *gig_dsp.py* for the file path if necessary.

### Generating Wish List

GIG - DSP will request two entries: a date and an amount.

The date, that must be in the 'YYYY-MM-DD' format, will be used to give the correct wish banner.

> For example: if the inserted date is '2020-10-31', the generator will consider the 'Sparkling Steps' banner to generate the wishes, with 'Klee' as the rate-up 5 star character and Xingqiu, Noelle and Sucrose as the rate-up 4 stars characters.

The amount is the number of wishes to be generated. For example: inserting '180' will generate 180 random entries for the .csv file, following the pity system rules.

### Saving the .csv file

After generating the desired amount of wishes, insert '-1' to end the generator. It will then request a name for the .csv file to be saved.

* The name does not require the '.csv' extension. GIG - DSP will automatically add the extension if not present.
* By default, the file name will be 'genshin_dataset.csv'. In case no specific name is desired, it is possible to leave the entry empty, and GIG - DSP will automatically save the file with its default name.

> **WARNING: if generating a .csv file to use with GI-DA, it is strongly recommended that the name used is the default file name, since GI-DA still has no tool to validate the existence of a .csv file with a different name than the default one**.

### Genshin Impact References

To help with the GIG - DSP, you can check all Genshin Impact's banners [here](https://genshin-impact.fandom.com/wiki/Wishes/List).