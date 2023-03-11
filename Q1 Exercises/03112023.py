# I have a cat and a dog.
#
# I got them at the same time as kitten/puppy. That was humanYears years ago.
#
# Return their respective ages now as [humanYears,catYears,dogYears]
#
# NOTES:
#
# humanYears >= 1
# humanYears are whole numbers only
# Cat Years
# 15 cat years for first year
#     +9 cat years for second year
#     +4 cat years for each year after that
# Dog Years
# 15 dog years for first year
#     +9 dog years for second year
#     +5 dog years for each year after that
# References
#
# http://www.catster.com/cats-101/calculate-cat-age-in-cat-years
# http://www.slate.com/articles/news_and_politics/explainer/2009/05/a_dogs_life.html

def human_years_cat_years_dog_years(human_years):
    cat_years = 15
    dog_years = 15
    if human_years == 1:
        return [1, cat_years, dog_years]
    elif human_years == 2:
        return [2, cat_years+9, dog_years+9]
    else:
        return [human_years, (cat_years+9)+((human_years-2)*4), (dog_years+9)+((human_years-2)*5)]

print(human_years_cat_years_dog_years(1)) # => [1,15,15])
print(human_years_cat_years_dog_years(2)) # => [2,24,24]
print(human_years_cat_years_dog_years(10)) # => [10,56,64]
