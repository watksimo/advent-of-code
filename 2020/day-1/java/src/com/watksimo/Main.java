package com.watksimo;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;

public class Main {
    private static int partOne(String inputFile) throws Exception {
        try {
            ArrayList<String> inputValues = new ArrayList<>(Files.readAllLines(Paths.get(inputFile)));
            for(int idx1=0; idx1<inputValues.size(); idx1++) {
                int val1 = Integer.valueOf(inputValues.get(idx1));
                for(int idx2=idx1; idx2<inputValues.size(); idx2++) {
                    int val2 = Integer.valueOf(inputValues.get(idx2));
                    if(val1 + val2 == 2020) {
                        return(val1 * val2);
                    }
                }
            }
            throw new Exception("No solution to part 1.");
        } catch (IOException e) {
            throw new Exception("Could not open file.");
        }

    }

    private static int partTwo(String inputFile) throws Exception {
        try {
            ArrayList<String> inputValues = new ArrayList<>(Files.readAllLines(Paths.get(inputFile)));
            for (int idx1 = 0; idx1 < inputValues.size(); idx1++) {
                int val1 = Integer.valueOf(inputValues.get(idx1));
                for (int idx2 = idx1; idx2 < inputValues.size(); idx2++) {
                    int val2 = Integer.valueOf(inputValues.get(idx2));
                    for (int idx3 = idx2; idx3 < inputValues.size(); idx3++) {
                        int val3 = Integer.valueOf(inputValues.get(idx3));
                        if (val1 + val2 + val3 == 2020) {
                            return (val1 * val2 * val3);
                        }
                    }
                }
            }
            throw new Exception("No solution to part 2.");
        } catch (IOException e) {
            throw new Exception("Could not open file.");
        }
    }

    public static void main(String[] args) {
        int[] testArray = new int[]{1721, 979, 366, 299, 675, 1456};

        try {
            int partOneSolution = partOne("../expense_report.txt");
            int partTwoSolution = partTwo("../expense_report.txt");
            System.out.printf("Part 1 solution is: %d%n", partOneSolution);
            System.out.printf("Part 2 solution is: %d%n", partTwoSolution);
        } catch(Exception e) {
            System.out.println(e);
        }
    }
}