package com.example.a7last.model.statement;

import com.example.a7last.exceptions.InterpreterException;
import com.example.a7last.model.expression.IExpression;
import com.example.a7last.model.programState.ProgramState;
import com.example.a7last.model.type.StringType;
import com.example.a7last.model.type.Type;
import com.example.a7last.model.utils.MyIDictionary;
import com.example.a7last.model.value.StringValue;
import com.example.a7last.model.value.Value;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;

public class OpenReadFile implements IStatement{
    private final IExpression expression;

    public OpenReadFile(IExpression expression) {
        this.expression = expression;
    }

    @Override
    public ProgramState execute(ProgramState state) throws InterpreterException {
        Value value = expression.eval(state.getSymTable(), state.getHeap());
        if (value.getType().equals(new StringType())) {
            StringValue fileName = (StringValue) value;
            MyIDictionary<String, BufferedReader> fileTable = state.getFileTable();
            if (!fileTable.isDefined(fileName.getValue())) {
                BufferedReader br;
                try {
                    br = new BufferedReader(new FileReader(fileName.getValue()));
                } catch (FileNotFoundException e) {
                    throw new InterpreterException(String.format("%s could not be opened", fileName.getValue()));
                }
                fileTable.put(fileName.getValue(), br);
                state.setFileTable(fileTable);
            } else {
                throw new InterpreterException(String.format("%s is already opened", fileName.getValue()));
            }
        } else {
            throw new InterpreterException(String.format("%s does not evaluate to StringType", expression));
        }
        return null;
    }

    @Override
    public MyIDictionary<String, Type> typeCheck(MyIDictionary<String, Type> typeEnv) throws InterpreterException {
        if (expression.typeCheck(typeEnv).equals(new StringType()))
            return typeEnv;
        else
            throw new InterpreterException("OpenReadFile requires a string expression.");
    }

    @Override
    public IStatement deepCopy() {
        return new OpenReadFile(expression.deepCopy());
    }

    @Override
    public String toString() {
        return String.format("OpenReadFile(%s)", expression.toString());
    }
}
