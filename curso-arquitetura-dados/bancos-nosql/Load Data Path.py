from typing import Protocol
import pandas as pd
from typing import Any


class DataloaderProtocol(Protocol):
    def read(*args, **kwargs) -> pd.DataFrame: ...
    def send(df: pd.DataFrame, *args, **kwargs): ...


class LocalDataLoader(DataloaderProtocol):
    def read(path: str) -> pd.DataFrame:
        return pd.read_csv(path)
    def send(df: pd.DataFrame, path: str):
        df.to_csv(path)



class DBDataloader(DataloaderProtocol):
    def __init__(self, *args, **kwargs):
        '''Create Conncetion'''
    
    def read(table_name: str) -> pd.DataFrame:
        '''Logic to load table'''
    
    def send(df: pd.DataFrame, table_name: str):
        '''logic to store table'''

def my_pipeline(
        data_loader: DataloaderProtocol,
        data_loader_kwargs_kwargs: dict[str, Any] = {},
        *args,
        **kwargs,
):
    data_loader = data_loader(**data_loader_kwargs_kwargs)
    df = data_loader.read(...)
    ...
    data_loader.send(df, ...)

class MyPipeline:
    def __init__(
            self,
            data_loader = DataloaderProtocol,
            data_loader_kwargs_kwargs = dict[str, Any] = {},
):
        self.data_loader: DataloaderProtocol = data_loader(**data_loader_kwargs_kwargs)

def run(self):
    df = self.data_loader.read(...)
    ...
    self.data_loader.send(df, ...)
    