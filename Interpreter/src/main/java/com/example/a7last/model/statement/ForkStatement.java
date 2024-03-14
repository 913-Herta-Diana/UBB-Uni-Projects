package com.example.a7last.model.statement;

import com.example.a7last.exceptions.InterpreterException;
import com.example.a7last.model.programState.ProgramState;
import com.example.a7last.model.type.Type;
import com.example.a7last.model.utils.MyDictionary;
import com.example.a7last.model.utils.MyIDictionary;
import com.example.a7last.model.utils.MyIStack;
import com.example.a7last.model.utils.MyStack;
import com.example.a7last.model.value.Value;

import java.util.Map;

public class ForkStatement implements IStatement{
    private final IStatement statement;

    public ForkStatement(IStatement statement) {
        this.statement = statement;
    }
    @Override
    public ProgramState execute(ProgramState state) throws InterpreterException {
        MyIStack<IStatement> newStack = new MyStack<>();
        newStack.push(statement);
        MyIDictionary<String, Value> newSymTable = new MyDictionary<>();
        for (Map.Entry<String, Value> entry: state.getSymTable().getContent().entrySet()) {
            newSymTable.put(entry.getKey(), entry.getValue().deepCopy());
        }

        return new ProgramState(newStack, newSymTable, state.getOut(), state.getFileTable(), state.getHeap());
    }

    @Override
    public MyIDictionary<String, Type> typeCheck(MyIDictionary<String, Type> typeEnv) throws InterpreterException {
        statement.typeCheck(typeEnv.deepCopy());
        return typeEnv;
    }

    @Override
    public IStatement deepCopy() {
        return new ForkStatement(statement.deepCopy());
    }

    @Override
    public String toString() {
        return String.format("Fork(%s)", statement.toString());
    }
}
