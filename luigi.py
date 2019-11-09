"""

Define .write(), .exists() atomically for a target
May never return True for an incomplete or failed output
A task is runnable when all input targets .exists()
A task is done when its output target .exists()

"""
