package com.example.a7last.model.statement;

import com.example.a7last.exceptions.InterpreterException;
import com.example.a7last.model.programState.ProgramState;
import com.example.a7last.model.type.Type;
import com.example.a7last.model.utils.MyIDictionary;

public interface IStatement {
    ProgramState execute(ProgramState state) throws InterpreterException;
    MyIDictionary<String, Type> typeCheck(MyIDictionary<String, Type> typeEnv) throws InterpreterException;
    IStatement deepCopy();
}
