"""
pages/github_config.py
---------------------
This module contains the code for Another Page of the Streamlit app.

The `main` function sets the title and writes a message for Another Page.
"""

import streamlit as st


def main():
    """
    This is the main function for the Another Page of the Streamlit app.
    It sets the title and writes a message for the page.
    """
    st.title("GitHub Configuration")
    st.write("This step walks through configuring branch protection rules in GitHub.")
    st.divider()

    # Branch protection rules
    st.markdown("1. From the project repository on GitHub, click on the `Settings` tab.")

    # Ruleset instructions
    st.subheader("Branch Ruleset")
    ruleset_instructions = """
    2. Access Rulesets:
        - Click on the `Rules` dropdown in the left sidebar, then click on `Rulesets`.
        - Click on the green `New ruleset` button in the top right corner.
        - Click `New branch ruleset` from the dropdown.
    """ # noqa W291
    st.markdown(ruleset_instructions)
    st.image(
        "images/github_create_ruleset.png",
        width=300,
        caption="Creating a new ruleset",
    )
    ruleset_instructions = """
    3. Configure the Ruleset:
        - Under `Ruleset Name`, enter `CI/CD Workflow`, or a name that makes sense for your project.
        - Set `Enforcement status` to `Active`.
        - Under `Targets -> Target branches`, click the dropdown button `Add target` and select
            `Include by pattern`.
        - Enter `"main", "develop"` under `Branch naming pattern` in the modal, then click `Add
            includsion pattern`.
        - Under `Rules -> Branch rules` make sure the following are checked:
            - `Restrict deletions`
            - `Require a pull request before merging`
            - `Require status checks to pass`
                - Click the dropdown button `Add checks`, type `build` in the search box, then click
                    `Add build`. *Note: `build` comes from the name of the `job` in `ci-cd.yml`.
                - Click the `Any source` button to the right in the recently added check, then
                    click `GitHub Actions`.
            - `Block force pushes`
    """ # noqa W291
    st.markdown(ruleset_instructions)
    st.image(
        "images/github_branch_naming_pattern.png",
        width=300,
        caption="Branch naming pattern for the main and develop branches",
    )
    st.image(
        "images/github_branch_targeting_criteria.png",
        width=300,
        caption="Branch targeting criteria",
    )
    st.image(
        "images/github_add_check.png",
        width=300,
        caption="Add a check to status checks",
    )
    st.image(
        "images/github_set_check_source.png",
        width=300,
        caption="Set the source of the check to GitHub Actions",
    )
    st.image(
        "images/github_selected_branch_rules.png",
        width=300,
        caption="Selected branch rules",
    )
    ruleset_instructions = """
    4. Save the Ruleset:
        - Click the green `Create` button at the bottom of the page.
    """ # noqa W291
    st.markdown(ruleset_instructions)
    st.image(
        "images/github_success_create_ruleset.png",
        width=300,
        caption="Ruleset created successfully",
    )

    # Classic branch protection rules
    st.subheader("Classic Branch Protection Rule")
    classic_instructions = """
    2. Access Branch Protection Rules:  
        - Click on the `Branches` tab in the left sidebar.
        - Click on the `Add rule` button.
    3. Configure the Branch Protection Rules:  
        - Under `Branch name pattern`, enter `main`.
        - Check the box for `Require a pull request before merging`.
        - Check `Require status checks to pass before merging` and check the box for `Require branches to be up to date before merging`.
        - In the search box, type the name of the CI/CD workflow that runs on GitHub Actions.  
        *Note: The name of the CI/CD workflow comes from the `ci-cd.yml` file in `.github/workflows`.*
        - Repeat the above steps for the `develop` branch.  
    
    At this point, the branch protection rules should look something like this:
    """  # noqa W291
    st.markdown(classic_instructions)
    st.image(
        "images/github_branchProtectionRule.png",
        width=300,
        caption="Branch Protection Rules for the main branch",
    )


if __name__ == "__main__":
    main()
