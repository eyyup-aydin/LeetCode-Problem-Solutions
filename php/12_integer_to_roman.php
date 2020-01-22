<?php

class Solution_12
{

  /**
   * https://leetcode.com/problems/integer-to-roman/
   *
   * @param Integer $num
   * @return String
   */
  function intToRoman($num) {
    $dict = array(
      1000 => 'M',
      900 => 'CM',
      500 => 'D',
      400 => 'CD',
      100 => 'C',
      90 => 'XC',
      50 => 'L',
      40 => 'XL',
      10 => 'X',
      9 => 'IX',
      5 => 'V',
      4 => 'IV',
      1 => 'I',
    );
    $result = "";
    foreach ($dict as $key => $value) {
      $p = intdiv($num, $key);
      $num %= $key;
      $result = $result . str_repeat($value, $p);
    }
    return $result;
  }
}

$sol = new Solution_12();
$res = $sol->intToRoman(4);
$res = $sol->intToRoman(9);
$res = $sol->intToRoman(40);
$res = $sol->intToRoman(90);
$res = $sol->intToRoman(400);
$res = $sol->intToRoman(900);
$res = $sol->intToRoman(49);
$res = $sol->intToRoman(1994);
$res = $sol->intToRoman(3999);

