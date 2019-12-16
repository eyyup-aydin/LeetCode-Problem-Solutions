<?php

class Solution {

  /**
  * @param Integer[][] $matrix
  * @return NULL
  */
  function rotate(&$matrix) {
    $len = count($matrix);

    for ($i = 0; $i < $len / 2; ++$i) {
      for ($j = $i; $j < $len - $i - 1; ++$j) {
        $temp = $matrix[$i][$j];
        $matrix[$i][$j] = $matrix[$len - 1 - $j][$i];
        $matrix[$len - 1 - $j][$i] = $matrix[$len - 1 - $i][$len - 1 - $j];
        $matrix[$len - 1 - $i][$len - 1 - $j] = $matrix[$j][$len - 1 - $i];
        $matrix[$j][$len - 1 - $i] = $temp;
      }
    }
  }

  function printMatrix(&$matrix)
  {
    $len = count($matrix);
    echo "============\n";
    for ($i = 0; $i < $len; $i++)
    {
      for ($j = 0; $j < $len; $j++)
        echo $matrix[$i][$j] . " ";
      echo "\n";
    }
    echo "============\n";
  }
}

$matrix = array
(
  array(1, 2, 3),
  array(4, 5, 6),
  array(7, 8, 9)
);

$sol = new Solution();
$sol->rotate($matrix);
$sol->printMatrix($matrix);