package com.watksimo;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;

public class Main {

    public static int partOne(List<String> inputList) {
        int validCount = 0;
        for(int i=0; i<inputList.size(); i++) {
            int minVal;
            int maxVal;
            char ruleChar;
            String password;

            String[] splitOne = inputList.get(i).split(":");
            password = splitOne[1].trim();
            String[] splitTwo = splitOne[0].split(" ");
            ruleChar = splitTwo[1].charAt(0);
            String[] splitThree = splitTwo[0].split("-");
            minVal = Integer.valueOf(splitThree[0]);
            maxVal = Integer.valueOf(splitThree[1]);

            int charCount = (int)password.chars().filter(ch -> ch == ruleChar).count();
            if(charCount >= minVal && charCount <= maxVal) {
                validCount++;
            }
        }
        return(validCount);
    }

    public static int partTwo(List<String> inputList) {
        int validCount = 0;
        for(String inputVal : inputList) {
            int firstVal;
            int lastVal;
            char ruleChar;
            String password;


            String[] splitOne = inputVal.split(":");
            password = splitOne[1].trim();
            String[] splitTwo = splitOne[0].split(" ");
            ruleChar = splitTwo[1].charAt(0);
            String[] splitThree = splitTwo[0].split("-");
            firstVal = Integer.valueOf(splitThree[0]);
            lastVal = Integer.valueOf(splitThree[1]);

            char existsVal = password.charAt(firstVal - 1);
            char nonexistVal = password.charAt(lastVal - 1);

            boolean b = (existsVal == ruleChar) ^ (nonexistVal == ruleChar);

            if(b) {
                validCount++;
            }
        }
        return(validCount);
    }

    public static void main(String[] args) throws IOException {
        List<String> inputValues = new ArrayList<>(Files.readAllLines(Paths.get("../password_list.txt")));
//        List<String> inputValues = new ArrayList<>(Files.readAllLines(Paths.get("../test-input.txt")));

        int partOneValid = partOne(inputValues);
        int partTwoValid = partTwo(inputValues);

        System.out.printf("Part 1: %d valid passwords.%n", partOneValid);
        System.out.printf("Part 2: %d valid passwords.%n", partTwoValid);

    }
}