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
import java.io.IOException;

public class CloseReadFile implements IStatement{
    private final IExpression expression;

    public CloseReadFile(IExpression expression) {
        this.expression = expression;
    }

    @Override
    public ProgramState execute(ProgramState state) throws InterpreterException {
        Value value = expression.eval(state.getSymTable(), state.getHeap());
        if (value.getType().equals(new StringType())) {
            StringValue fileName = (StringValue) value;
            MyIDictionary<String, BufferedReader> fileTable = state.getFileTable();
            if (fileTable.isDefined(fileName.getValue())) {
                BufferedReader br = fileTable.lookUp(fileName.getValue());
                try {
                    br.close();
                } catch (IOException e) {
                    throw new InterpreterException(String.format("Unexpected error in closing %s", value));
                }
                fileTable.remove(fileName.getValue());
                state.setFileTable(fileTable);
            } else
                throw new InterpreterException(String.format("%s is not present in the FileTable", value));
        } else
            throw new InterpreterException(String.format("%s does not evaluate to StringValue", expression));
        return null;
    }

    @Override
    public MyIDictionary<String, Type> typeCheck(MyIDictionary<String, Type> typeEnv) throws InterpreterException {
        if (expression.typeCheck(typeEnv).equals(new StringType()))
            return typeEnv;
        else
            throw new InterpreterException("CloseReadFile requires a string expression.");

    }

    @Override
    public IStatement deepCopy() {
        return new CloseReadFile(expression.deepCopy());
    }

    @Override
    public String toString() {
        return String.format("CloseReadFile(%s)", expression.toString());
    }
}
