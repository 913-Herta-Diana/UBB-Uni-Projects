package com.example.a7last.view;

import com.example.a7last.exceptions.InterpreterException;
import com.example.a7last.model.utils.MyDictionary;
import com.example.a7last.model.utils.MyIDictionary;

import java.util.Scanner;

public class TextMenu {
    private MyIDictionary<String, Command> commands;

    public TextMenu() {
        this.commands = new MyDictionary<>();
    }

    public void addCommand(Command command) {
        this.commands.put(command.getKey(), command);
    }

    private void printMenu() {
        for (Command command: commands.values()) {
            String line = String.format("%4s: %s", command.getKey(), command.getDescription());
            System.out.println(line);
        }
    }

    public void show() {
        Scanner scanner = new Scanner(System.in);
        while (true) {
            printMenu();
            System.out.println("Input the option: ");
            String key = scanner.nextLine();
            try {
                Command command = commands.lookUp(key);
                command.execute();
            } catch (InterpreterException e) {
                e.printStackTrace();
            }
        }
    }
}
