package com.example.a7last.model.statement;

import com.example.a7last.exceptions.InterpreterException;
import com.example.a7last.model.programState.ProgramState;
import com.example.a7last.model.type.Type;
import com.example.a7last.model.utils.MyIDictionary;
import com.example.a7last.model.value.Value;

public class VariableDeclarationStatement implements IStatement {
    String name;
    Type type;

    public VariableDeclarationStatement(String name, Type type) {
        this.name = name;
        this.type = type;
    }

    @Override
    public ProgramState execute(ProgramState state) throws InterpreterException {
        MyIDictionary<String, Value> symTable = state.getSymTable();
        if (symTable.isDefined(name)) {
            throw new InterpreterException("Variable " + name + " already exists in the symTable.");
        }
        symTable.put(name, type.defaultValue());
        state.setSymTable(symTable);
        return null;
    }

    @Override
    public MyIDictionary<String, Type> typeCheck(MyIDictionary<String, Type> typeEnv) throws InterpreterException {
        typeEnv.put(name, type);
        return typeEnv;
    }

    @Override
    public IStatement deepCopy() {
        return new VariableDeclarationStatement(name, type);
    }

    @Override
    public String toString() {
        return String.format("%s %s", type.toString(), name);
    }
}

