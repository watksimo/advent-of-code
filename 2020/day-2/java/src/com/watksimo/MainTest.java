package com.watksimo;

import org.junit.jupiter.api.Test;

import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;

import static org.junit.jupiter.api.Assertions.*;

class MainTest {

    private Main main;

    @Test
    public void testPartTwo_One() {
        ArrayList<String> testInput = new ArrayList<String>(Arrays.asList("1-3 a: abcde"));
        int partTwo = Main.partTwo(testInput);
        assertEquals(partTwo, 1);
    }

    @Test
    public void testPartTwo_Two() {
        ArrayList<String> testInput = new ArrayList<String>(Arrays.asList("1-3 b: cdefg"));
        int partTwo = Main.partTwo(testInput);
        assertEquals(0, partTwo);
    }

    @Test
    public void testPartTwo_Three() {
        ArrayList<String> testInput = new ArrayList<String>(Arrays.asList("2-9 c: ccccccccc"));
        int partTwo = Main.partTwo(testInput);
        assertEquals(0, partTwo);
    }

    @Test
    public void testPartTwo_Four() {
        ArrayList<String> testInput = new ArrayList<String>(Arrays.asList("1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"));
        int partTwo = Main.partTwo(testInput);
        assertEquals(1, partTwo);
    }

    @Test
    public void testPartTwo_Five() {
        ArrayList<String> testInput = new ArrayList<String>(Arrays.asList("1-3 a: cbade"));
        int partTwo = Main.partTwo(testInput);
        assertEquals(1, partTwo);
    }

}