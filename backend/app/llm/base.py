from abc import ABC, abstractmethod
from dataclasses import dataclass
@dataclass
class LLMResult: text:str; model:str; provider:str
class LLMProvider(ABC):
 @abstractmethod
 async def generate(self, system:str, messages:list[dict], temperature:float=0.2, max_tokens:int=1800)->LLMResult: ...
 @abstractmethod
 async def health(self)->dict: ...
