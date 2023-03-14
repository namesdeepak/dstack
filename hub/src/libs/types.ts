export type FormFieldError = {
    loc: string[];
    msg: string;
    type: string;
};

export type FormErrors = {
    detail: FormFieldError[];
};

export type RequestErrorWithDetail = {
    detail: string;
};
