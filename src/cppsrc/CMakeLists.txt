add_library (Animals "cats.cpp" "cats.h")
target_include_directories(Animals PUBLIC .)

# Should install library properly here, but I'm focusing on just the docs
