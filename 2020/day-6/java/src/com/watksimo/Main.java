package com.watksimo;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.*;

public class Main
{

    private static List<String> separateGroups(List<String> inputList) {
        ArrayList<String> groupList = new ArrayList<String>();
        String groupAnswers = "";
        for(int i=0; i<inputList.size(); i++) {
            String listVal = inputList.get(i);
            if(listVal.trim().equals("")) {
                if(groupAnswers != "") {
                    groupList.add(groupAnswers);
                }
                groupAnswers = "";
            } else {
                groupAnswers += listVal;
            }
        }
        if(groupAnswers != "") {
            groupList.add(groupAnswers);
        }
        return groupList;
    }

    public static ArrayList<String> removeDuplicates(List<String> inputArray) {
        ArrayList<String> noDupList = new ArrayList<>();

        for(int i=0; i<inputArray.size(); i++) {
            Set<Character> noDupSet = new HashSet<>();
            String noDupAnswers = "";
            String listVal = inputArray.get(i);

            for(int j=0; j<listVal.length(); j++) {
                char answerChar = listVal.charAt(j);
                if(noDupSet.add(answerChar)) {
                    noDupAnswers = noDupAnswers + answerChar;
                }
            }
            noDupList.add(noDupAnswers);
        }
        System.out.println(noDupList);
        return noDupList;
    }

    public static int partOne(List<String> inputArray) {

        List<String> groupList = separateGroups(inputArray);
        List<String> noDupList = removeDuplicates(groupList);

        int answerSum = 0;
        for(int i=0; i<noDupList.size(); i++) {
            answerSum = answerSum + noDupList.get(i).length();
        }
        return answerSum;
    }

    public static void main(String[] args) throws IOException {
        List<String> inputValues = new ArrayList<String>(Files.readAllLines(Paths.get("../real-input.txt")));

        System.out.printf("Part 1: Solution is %d.%n", partOne(inputValues));

    }
}