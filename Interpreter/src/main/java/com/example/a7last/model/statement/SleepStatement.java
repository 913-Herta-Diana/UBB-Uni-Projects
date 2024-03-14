package com.example.a7last.model.statement;

import com.example.a7last.exceptions.InterpreterException;
import com.example.a7last.model.programState.ProgramState;
import com.example.a7last.model.type.Type;
import com.example.a7last.model.utils.MyIDictionary;
import com.example.a7last.model.utils.MyIStack;

public class SleepStatement implements IStatement{
    private final int value;

    public SleepStatement(int value) {
        this.value = value;
    }

    @Override
    public ProgramState execute(ProgramState state) throws InterpreterException {
        if (value != 0) {
            MyIStack<IStatement> exeStack = state.getExeStack();
            exeStack.push(new SleepStatement(value - 1));
            state.setExeStack(exeStack);
        }
        return null;
    }

    @Override
    public MyIDictionary<String, Type> typeCheck(MyIDictionary<String, Type> typeEnv) throws InterpreterException {
        return typeEnv;
    }

    @Override
    public IStatement deepCopy() {
        return new SleepStatement(value);
    }

    @Override
    public String toString() {
        return String.format("sleep(%s)", value);
    }
}