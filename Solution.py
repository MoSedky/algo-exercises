import array
def get_sum (input_array):
   array_Length=len(input_array)
   if(array_Length < 4):                                        # Check Array Length to be more than 4
       print("Rejected Array for length less than 4 ")
   else:

           if(isinstance(input_array, float)):                  # Check Array data types
               print("Rejected Array for contains Float numbers")
           else:
               sorted_array=sorted(input_array)                 # Sort Array in ASC Order
               print("Sorted Array is", sorted_array)

               return_value=sorted_array[0]+sorted_array[1]     # Get sum of two lowest numbers in Sorted Array

               return return_value                              # Return Sum of two least numbers


a = array.array('i', [5999, 55, 100, 77, 256, 899, 20, 23, 258, 10, 5, 2, 22, 220])
sum_value = get_sum(a)
print("Sum of two lowest positive integers is: ", sum_value)