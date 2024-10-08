import "./style/main_input.sass"

export function MainInput({ lblText, register, errorsMessage, children, ...props }) {

    return(
        <div className="input__container">
            <input className="input-main" autocomplete="off"  {...register} {...props}/>
            <label className="input-lbl">
                <p className="input-lbl-text">{ lblText }</p>
            </label>
            { children }
            <label className="label-error">
                { errorsMessage }
            </label> 
        </div>
    );
};
