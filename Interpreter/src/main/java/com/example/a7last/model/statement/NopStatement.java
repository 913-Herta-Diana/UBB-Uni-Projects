package com.example.a7last.model.statement;

import com.example.a7last.exceptions.InterpreterException;
import com.example.a7last.model.programState.ProgramState;
import com.example.a7last.model.type.Type;
import com.example.a7last.model.utils.MyIDictionary;

public class NopStatement implements IStatement {
    @Override
    public ProgramState execute(ProgramState state) throws InterpreterException {
        return null;
    }

    @Override
    public MyIDictionary<String, Type> typeCheck(MyIDictionary<String, Type> typeEnv) throws InterpreterException {
        return typeEnv;
    }

    @Override
    public IStatement deepCopy() {
        return new NopStatement();
    }

    @Override
    public String toString() {
        return "NopStatement";
    }
}
