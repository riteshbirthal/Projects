#include <stdio.h>
#include <time.h>

/*
    Sudoku Representation
    
  *****************************
  *****************************
  ** Box 1 ** Box 2 ** Box 3 **
  *****************************
  *****************************
  ** Box 4 ** Box 5 ** Box 6 **
  *****************************
  *****************************
  ** Box 7 ** Box 8 ** Box 9 **
  *****************************
  *****************************
*/
//Element Checker Function
int CheckElement (int arr[][9], int i, int j, int element)
{
  //printf("Checking element = %d, for i = %d, j = %d \n",element, i,j);
  int t, p, q;
  //Checking Column Elements
  for (t = 0; t < 9; t++)
    {
      if (t != i && arr[t][j] == element)
	{
	  return 0;
	}
    }
  //Checking Row Elements
  for (t = 0; t < 9; t++)
    {
      if (t != j && arr[i][t] == element)
	{
	  return 0;
	}
    }
  //Checking Box 1 Elements
  if (i >= 0 && i < 3 && j >= 0 && j < 3)
    {
      for (p = 0; p < 3; p++)
	{
	  for (q = 0; q < 3; q++)
	    {
	      if ((p != i || q != j) && arr[p][q] == element)
		{
		  return 0;
		}
	    }
	}
    }
  //Checking Box 4 Elements
  else if (i >= 3 && i < 6 && j >= 0 && j < 3)
    {
      for (p = 3; p < 6; p++)
	{
	  for (q = 0; q < 3; q++)
	    {
	      if ((p != i || q != j) && arr[p][q] == element)
		{
		  return 0;
		}
	    }
	}
    }
  //Checking Box 7 Elements
  else if (i >= 6 && i < 9 && j >= 0 && j < 3)
    {
      for (p = 6; p < 9; p++)
	{
	  for (q = 0; q < 3; q++)
	    {
	      if ((p != i || q != j) && arr[p][q] == element)
		{
		  return 0;
		}
	    }
	}
    }
  //Checking Box 2 Elements
  else if (i >= 0 && i < 3 && j >= 3 && j < 6)
    {
      for (p = 0; p < 3; p++)
	{
	  for (q = 3; q < 6; q++)
	    {
	      if ((p != i || q != j) && arr[p][q] == element)
		{
		  return 0;
		}
	    }
	}
    }
  //Checking Box 5 Elements
  else if (i >= 3 && i < 6 && j >= 3 && j < 6)
    {
      for (p = 3; p < 6; p++)
	{
	  for (q = 3; q < 6; q++)
	    {
	      if ((p != i || q != j) && arr[p][q] == element)
		{
		  return 0;
		}
	    }
	}
    }
  //Checking Box 8 Elements
  else if (i >= 6 && i < 9 && j >= 3 && j < 6)
    {
      for (p = 6; p < 9; p++)
	{
	  for (q = 3; q < 6; q++)
	    {
	      if ((p != i || q != j) && arr[p][q] == element)
		{
		  return 0;
		}
	    }
	}
    }
  //Checking Box 3 Elements
  else if (i >= 0 && i < 3 && j >= 6 && j < 9)
    {
      for (p = 0; p < 3; p++)
	{
	  for (q = 6; q < 9; q++)
	    {
	      if ((p != i || q != j) && arr[p][q] == element)
		{
		  return 0;
		}
	    }
	}
    }
  //Checking Box 6 Elements
  else if (i >= 3 && i < 6 && j >= 6 && j < 9)
    {
      for (p = 3; p < 6; p++)
	{
	  for (q = 6; q < 9; q++)
	    {
	      if ((p != i || q != j) && arr[p][q] == element)
		{
		  return 0;
		}
	    }
	}
    }
  //Checking Box 9 Elements
  else if (i >= 6 && i < 9 && j >= 6 && j < 9)
    {
      for (p = 6; p < 9; p++)
	{
	  for (q = 6; q < 9; q++)
	    {
	      if ((p != i || q != j) && arr[p][q] == element)
		{
		  return 0;
		}
	    }
	}
    }

  return 1;
}

int SudokuSolver (int arr[][9], int i, int j, int s)
{
  if (s == 81)
    {
      int sum = 0;
      for (int p = 0; p < 9; p++)
	{
	  for (int q = 0; q < 9; q++)
	    {
	      if (arr[p][q])
		{
		  sum++;
		}
	    }
	}
      if (sum != 81)
	{
	  //printf("Returning for sum = %d \n", sum);
	  return 0;
	}
      else
	{
	  //printf("Returning for sum = %d \n", sum);
	  return 1;
	}
    }
  if (arr[i][j] && j != 8)
    {
      //printf("Calling fun for i = %d, j = %d, s = %d \n", i,j+1,s+1);
      return SudokuSolver (arr, i, j + 1, s + 1);
    }
  else if (arr[i][j])
    {
      //printf("Calling fun for i = %d, j = %d, s = %d \n", i+1,0,s+1);
      return SudokuSolver (arr, i + 1, 0, s + 1);
    }
  int l;
  for (int p = 1; p < 10; p++)
    {
      //printf("p = %d \n", p);
      if (CheckElement (arr, i, j, p))
	{
	  l = 1;
	  arr[i][j] = p;
	  int t;
	  if (j != 8)
	    {
	      //printf("Calling fun for i = %d, j = %d, s = %d \n", i,j+1,s+1);
	      t = SudokuSolver (arr, i, j + 1, s + 1);
	    }
	  else
	    {
	      //printf("Calling fun for i = %d, j = %d, s = %d \n", i+1,0,s+1);
	      t = SudokuSolver (arr, i + 1, 0, s + 1);
	    }
	  if (!t)
	    {
	      l = 0;
	      arr[i][j] = 0;
	    }
	}
    }
  if (!l)
    return 0;
}

int main ()
{
  time_t start, end;
  int arr[9][9] = {
    {5, 0, 0, 0, 0, 0, 0, 7, 0},
    {0, 1, 0, 3, 0, 9, 8, 0, 0},
    {0, 0, 0, 0, 4, 0, 0, 0, 0},

    {0, 0, 1, 0, 0, 0, 0, 0, 9},
    {0, 0, 0, 0, 0, 6, 0, 0, 0},
    {0, 9, 0, 2, 0, 8, 3, 0, 0},

    {0, 0, 7, 4, 0, 2, 0, 8, 0},
    {0, 2, 0, 0, 6, 0, 0, 0, 0},
    {0, 0, 0, 0, 1, 0, 4, 0, 0}
  };
  char arr2[81];
  int arr3[9][9];
  printf ("Follow the below rules for entries.\n");
  printf ("  1. For blank entries use spaces\n");
  printf ("  2. For filled entries use numbers.\n");
  printf ("  3. Write all entries in one line as given below.\n");
  printf ("For example:-\n");
  for (int i = 0; i < 9; i++)
    {
      if (i % 3 == 0)
	printf ("\n");
      for (int j = 0; j < 9; j++)
	{
	  if (j % 3 == 0)
	    printf ("  ");
	  printf ("%d ", arr[i][j]);
	}
      printf ("\n");
    }
  printf ("\nThe above sudoku can be written as:-\n");
  printf
    ("5      7  1 3 98      4      1     9     6    9 2 83    74 2 8  2  6        1 4  \n \n");
  printf ("Please enter the values. \n");
  for (int i = 0; i < 81; i++)
    {
      scanf ("%c", &arr2[i]);
      if ((arr2[i] == ' ') || (arr2[i] >= '1' && arr2[i] <= '9'))
	{
	  continue;
	}
      else
	{
	  printf ("Please input valid entry.\n");
	  return 0;
	}
    }
  for (int i = 0; i < 81; i++)
    {
      if (arr2[i] >= '1' && arr2[i] <= '9')
	{
	  arr3[i / 9][i % 9] = arr2[i] - '0';
	}
      else
	{
	  arr3[i / 9][i % 9] = 0;
	}
    }
  start = time (NULL);
  for (int i = 0; i < 9; i++)
    {
      for (int j = 0; j < 9; j++)
	{
	  SudokuSolver (arr3, 0, 0, 0);
	}
    }
  end = time (NULL);
  printf ("\n");
  printf ("Your Solved Sudoku is-\n");
  for (int i = 0; i < 9; i++)
    {
      if (i % 3 == 0)
	printf ("\n");
      for (int j = 0; j < 9; j++)
	{
	  if (j % 3 == 0)
	    printf ("  ");
	  printf ("%d ", arr3[i][j]);
	}
      printf ("\n");
    }
  printf ("\nTime taken to solve the sudoku is %f seconds",
	  difftime (end, start));
  return 0;
}