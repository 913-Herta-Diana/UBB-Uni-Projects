package com.example.a7last.model.type;

import com.example.a7last.model.value.BoolValue;
import com.example.a7last.model.value.Value;

public class BoolType implements Type{
    @Override
    public boolean equals(Type anotherType) {
        return anotherType instanceof BoolType;
    }

    @Override
    public Value defaultValue() {
        return new BoolValue(false);
    }

    @Override
    public Type deepCopy() {
        return new BoolType();
    }

    @Override
    public String toString() {
        return "bool";
    }
}
