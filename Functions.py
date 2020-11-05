#SIMPLE ADDITION EXAMPLE
def addition(num1, num2):          #define function with def and function name
    answer = num1+num2
    return answer

#print(addition(1,3))                     #call the function

                #MORE REALISTIC EXAMPLE - DEFINE A WEBSITE
#########################################################################
'''
def website(font, background_colour, font_size, font_colour):
    print('Font:', font)
    print('Background Colour:', background_colour)
    print('Font Size:', font_size)
    print('Font Colour:', font_colour)

#When defining a website, this could become incredibly long.
#Also with functions you have to maintain order... UNLESS instead of
        #website('Calibri','White',11,'Black')

#you do this
website(font_size = 11,
        font_colour = 'black',
        background_colour = 'white',
        font = 'calibri')
'''

#########################################################################
                     #Setting function parameter defaults
def website(font = 'calibri',
            background_colour = 'white',
            font_size = 11,
            font_colour = 'black'):
    print('Font:', font)
    print('Background Colour:', background_colour)
    print('Font Size:', font_size)
    print('Font Colour:', font_colour)

#Now the website parameters are default to ensure quick website development
#However, the user can choose to customise by overwriting these defaults
website(background_colour = 'grey') 







    
