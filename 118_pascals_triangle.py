    """
Create an empty list to store the triangle.
Loop over the range from 0 to numRows - 1, representing each row in the triangle.
Inside the loop, create an empty list to store the current row.
Loop over the range from 0 to the current row number, representing each position in the row.
Inside the inner loop, if the current position is the first or last in the row (position 0 or position equal to the current row number), append the number 1 to the current row list.
Otherwise, calculate the value of the current position as the sum of the two numbers directly above it in the previous row.
Append the value to the current row list.
After the inner loop completes for the current row, append the current row list to the triangle list.
After the outer loop completes for all rows, return the triangle list.
    """

def triangle(numRows): 

    triangle = [] 