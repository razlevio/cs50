#include "helpers.h"
#include <math.h>
#include <stdio.h>
#include <cs50.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            RGBTRIPLE pixel = image[i][j];
            int avg = round((pixel.rgbtRed + pixel.rgbtGreen + pixel.rgbtBlue) / 3.0);
            //image[i][j].rgbtRed = image[i][j].rgbtGreen = image[i][j].rgbtBlue = avg;
            image[i][j].rgbtRed = avg;
            image[i][j].rgbtGreen = avg;
            image[i][j].rgbtBlue = avg;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    //sepiaRed = .393 * originalRed + .769 * originalGreen + .189 * originalBlue
    //sepiaGreen = .349 * originalRed + .686 * originalGreen + .168 * originalBlue
    //sepiaBlue = .272 * originalRed + .534 * originalGreen + .131 * originalBlue
    
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            RGBTRIPLE pixel = image[i][j];
            int sepiaRed = round((.393 * pixel.rgbtRed) + (.769 * pixel.rgbtGreen) + (.189 * pixel.rgbtBlue));
            int sepiaGreen = round((.349 * pixel.rgbtRed) + (.686 * pixel.rgbtGreen) + (.168 * pixel.rgbtBlue));
            int sepiaBlue = round((.272 * pixel.rgbtRed) + (.534 * pixel.rgbtGreen) + (.131 * pixel.rgbtBlue));
            if (sepiaRed > 255)
            {
                sepiaRed = 255;
            }
            if (sepiaGreen > 255)
            {
                sepiaGreen = 255;
            }
            if (sepiaBlue > 255)
            {
                sepiaBlue = 255;
            }
            image[i][j].rgbtRed = sepiaRed;
            image[i][j].rgbtGreen = sepiaGreen;
            image[i][j].rgbtBlue = sepiaBlue;
        }
    }
    return;
}

void swap(RGBTRIPLE *pixel1, RGBTRIPLE *pixel2)
{
    RGBTRIPLE temp = *pixel1;
    *pixel1 = *pixel2;
    *pixel2 = temp;
}
// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width / 2; j++)
        {
            swap(&image[i][j], &image[i][width - 1 - j]);
        }
    }
}

bool is_valid_pixel(int i, int j, int height, int width)
{
    return i >= 0 && i < height && j >= 0 && j < width;
}

RGBTRIPLE get_blurred_pixel(int i, int j, int height, int width, RGBTRIPLE image[height][width])
{
    int redValue, blueValue, greenValue; 
    redValue = blueValue = greenValue = 0;
    int NumOfValidPixels = 0;
    for (int di = -1; di <= 1; di++)
    {
        for (int dj = -1; dj <= 1; dj++)
        {
            int new_i = i + di;
            int new_j = j + dj;
            if (is_valid_pixel(new_i, new_j, height, width))
            {
                NumOfValidPixels++;
                redValue += image[new_i][new_j].rgbtRed;
                blueValue += image[new_i][new_j].rgbtBlue;
                greenValue += image[new_i][new_j].rgbtGreen;
            }
        }
    }
    RGBTRIPLE blurred_pixel;
    blurred_pixel.rgbtRed = round((float) redValue / NumOfValidPixels);
    blurred_pixel.rgbtGreen = round((float) greenValue / NumOfValidPixels);
    blurred_pixel.rgbtBlue = round((float) blueValue / NumOfValidPixels);
    return blurred_pixel;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE new_image[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            new_image[i][j] = get_blurred_pixel(i, j, height, width, image);
        }
    }
    
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j] = new_image[i][j];
        }
    }
}
