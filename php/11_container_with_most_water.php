<?php

class Solution {

  /**
   * https://leetcode.com/problems/container-with-most-water/
   * 
   * @param Integer[] $height
   * @return Integer
   */
  function maxArea($height) {
    $maxArea = 0;

    $s = 0;
    $e = count($height) - 1;
    while ($s < $e) {
      $len = min($height[$s], $height[$e]);
      $maxArea = max($maxArea, $len * ($e - $s));
      if ($height[$s] < $height[$e])
        $s += 1;
      else
        $e -= 1;
    }
    return $maxArea;
  }
}

$sol = new Solution();
$arr = [1,8,6,2,5,4,8,3,7];

$res = $sol->maxArea($arr);
printf("res: %d\n", $res);

$res = $sol->maxArea([2,3,4,5,18,17,6]);
printf("res: %d\n", $res);